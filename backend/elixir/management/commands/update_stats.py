from django.core.management.base import BaseCommand, CommandError
from elixir.tasks import *
import json, os


class Command(BaseCommand):
	help = 'Update Tool Statistics'

	def handle(self, *args, **options):

		generate_missing_stats()

		self.stdout.write('All done.')
