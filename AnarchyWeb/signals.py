import os

from discord_webhook import DiscordEmbed, DiscordWebhook
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Hack


@receiver(pre_save, sender=Hack)
def client_pre_save(sender, instance, **kwargs):
    if instance.pk:
        instance._pre_save_instance = Hack.objects.get(pk=instance.pk)


@receiver(post_save, sender=Hack)
def client_post_save(sender, instance, created, **kwargs):
    if os.getenv("DISCORD_WEBHOOK_MODELS_LOGS"):
        changes = []

        if not created:
            print(f"Hack updated: {instance}")
            pre_save_instance = getattr(instance, "_pre_save_instance", None)
            if pre_save_instance:
                for field in instance._meta.fields:
                    field_name = field.name
                    old_value = getattr(pre_save_instance, field_name)
                    new_value = getattr(instance, field_name)
                    if old_value != new_value:
                        changes.append((field_name, old_value, new_value))

                if changes:
                    print("Changes:")
                    for field_name, old_value, new_value in changes:
                        print(f"{field_name}: {old_value} -> {new_value}")

        send_discord_log(instance, created, changes)

    else:
        print("DISCORD_WEBHOOK_MODELS_LOGS not set")


def send_discord_log(
    client_instance: Hack, created: bool = False, changes: list = None
):
    if created or (changes and not created):
        webhook = DiscordWebhook(url=os.getenv("DISCORD_WEBHOOK_MODELS_LOGS"))

        if created:
            embed = DiscordEmbed(
                title=f"New hack {client_instance.name} added!",
                description="",
                color="902bfb",
            )

            for field in client_instance._meta.fields:
                field_name = field.name

                field_value = getattr(client_instance, field_name)
                embed.add_embed_field(name=field_name, value=field_value, inline=True)

        else:
            embed = DiscordEmbed(
                title=f"Hack {client_instance.name} updated, changes: ",
                description="",
                color="902bfb",
            )

            if changes:
                for field_name, old_value, new_value in changes:
                    embed.add_embed_field(
                        name=field_name,
                        value=f"{old_value} -> {new_value}",
                        inline=False,
                    )

        webhook.add_embed(embed)
        webhook.execute()
