# Generated by Django 5.1.4 on 2024-12-13 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aves", "0004_rename_desconto_percentual_investidor_comissao_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cpf", models.CharField(max_length=11, unique=True)),
                ("nome_completo", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("telefone", models.CharField(max_length=15)),
                ("data_compra", models.DateField(blank=True, null=True)),
                (
                    "motivo_compra",
                    models.CharField(
                        choices=[
                            ("Criador", "Criador"),
                            ("Coleção", "Coleção"),
                            ("Pet", "Pet"),
                        ],
                        max_length=50,
                    ),
                ),
                ("preco_compra", models.DecimalField(decimal_places=2, max_digits=10)),
                ("notas_adicionais", models.TextField(blank=True, null=True)),
                (
                    "aves_compradas",
                    models.ManyToManyField(related_name="clientes_set", to="aves.ave"),
                ),
            ],
        ),
    ]