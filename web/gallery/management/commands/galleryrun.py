# -*- coding: utf-8 -*-
from django.core.files import File
from django.contrib.auth.models import User
import djclick as click
from gallery import models
import os
from logging import getLogger
log = getLogger()


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.argument('user_id')
@click.argument('path')
@click.pass_context
def add_imagefile(ctx, user_id, path):
    '''Add ImageFile'''
    name = os.path.basename(path)
    models.ImageFile.objects.create(
        user=User.objects.filter(id=user_id).first(),
        data=File(open(path), name=name))
