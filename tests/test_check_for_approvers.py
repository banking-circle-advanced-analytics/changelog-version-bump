from pytest import mark, raises
from changelog_version_bump.check_for_approvers.cli import process_file


@mark.parametrize("filename, raises_error", [
    ('tests/test_data/with_approvers.md', False),
    ('tests/test_data/approvers_not_selected.md', True),
    ('tests/test_data/no_approvers.md', False),
])
def test_check_for_approvers(filename, raises_error):
    if raises_error:
        with raises(ValueError):
            process_file(filename)
    else:
        process_file(filename)
        assert True