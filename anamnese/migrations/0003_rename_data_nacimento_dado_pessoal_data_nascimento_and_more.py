# Generated by Django 5.0.4 on 2024-04-26 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anamnese', '0002_rename_dados_pessoais_dado_pessoal_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dado_pessoal',
            old_name='data_nacimento',
            new_name='data_nascimento',
        ),
        migrations.RenameField(
            model_name='exame',
            old_name='doenças_atual',
            new_name='doencas_atual',
        ),
        migrations.RenameField(
            model_name='exame',
            old_name='doenças_familiares',
            new_name='doencas_familiares',
        ),
        migrations.RenameField(
            model_name='exame',
            old_name='doenças_pessoas',
            new_name='doencas_pessoais',
        ),
        migrations.RenameField(
            model_name='exame',
            old_name='exame_sanque',
            new_name='exame_sangue',
        ),
        migrations.RenameField(
            model_name='exame_hemograma',
            old_name='nivel_pressão_aterial',
            new_name='nivel_pressao_arterial',
        ),
        migrations.RenameField(
            model_name='exame_hemograma',
            old_name='nivel_trigicerideos',
            new_name='nivel_triglicerideos',
        ),
        migrations.RenameField(
            model_name='ficha',
            old_name='Dados_pessoais',
            new_name='dados_pessoais',
        ),
        migrations.RenameField(
            model_name='medico',
            old_name='ficha',
            new_name='fichas',
        ),
    ]
