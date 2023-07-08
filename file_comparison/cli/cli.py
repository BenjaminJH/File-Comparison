import click
from src.filtering.directory_comparer import DirectoryComparer


@click.command()
@click.option('--dir1', default=r'test_directory_a', help='Primary Directory')
@click.option('--dir2', default=r'test_directory_b', help='Secondary Directory')
@click.option('--search_type', default=r'path', help='[path|count]')
def run_comparison(dir1, dir2, search_type):
	directory_comparer = DirectoryComparer(dir1, dir2)
	if search_type == "path":
		print(directory_comparer.compare_by_file_path())
	elif search_type == "count":
		print(directory_comparer.compare_by_file_count())


if __name__ == "__main__":
	run_comparison()
