# Generated by Django 5.1.4 on 2024-12-13 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("aves", "0003_ave_data_morte_ave_motivo_morte_ave_preco_compra_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="investidor",
            old_name="desconto_percentual",
            new_name="comissao",
        ),
        migrations.RenameField(
            model_name="investidor",
            old_name="custo_mensal",
            new_name="custo_condominio",
        ),
        migrations.RenameField(
            model_name="investidor",
            old_name="nome",
            new_name="nome_completo",
        ),
        migrations.AddField(
            model_name="investidor",
            name="cpf",
            field=models.CharField(default="00000000000", max_length=11, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="investidor",
            name="data_inicio_investimento",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="investidor",
            name="filhotes",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="investidor",
            name="notas_adicionais",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="investidor",
            name="valor_investimento",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="investidor",
            name="aves",
            field=models.ManyToManyField(
                related_name="investidores_set", to="aves.ave"
            ),
        ),
    ]