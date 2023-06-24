import click
from src.filtering.compare import compare_by_file_path, compare_by_file_count

@click.command()
@click.option('--dir1', default=r'test_directory_a', help='Primary Directory')
@click.option('--dir2', default=r'test_directory_b', help='Secondary Directory')
@click.option('--search_type', default=r'path', help='[path|count]')
def run_comparison(dir1, dir2, search_type):
	if search_type == "path":
		compare_by_file_path(dir1, dir2)
	elif search_type == "count":
		compare_by_file_count(dir1, dir2)


if __name__ == "__main__":
	run_comparison()
