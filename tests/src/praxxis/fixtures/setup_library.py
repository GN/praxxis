"""
adds test library to temp directories and does a few useful operations on them
"""
import pytest

@pytest.fixture(scope="function")
def add_test_library(library_root, library_db, query_start, query_end):
    """
    copies test notebooks from the tests directory to the temp root, and loads them into the db
    """
    import os
    import shutil 
    from src.praxxis.library import sync_library
    from src.praxxis.library import remove_library
    from tests.src.praxxis.util import dummy_object
    from src.praxxis.util import rmtree
    from src.praxxis.util import copytree

    library_location = os.path.join(library_root, 'test_notebooks')
    
    copytree.copytree(os.path.join('tests', 'test_notebooks'), os.path.join(library_root,  'test_notebooks'), test=True)
    assert os.path.exists(library_location)

    sync_library.sync_library(library_root, library_db)   
    yield 

    dummy_library = dummy_object.make_dummy_library()
    remove_library.remove_library(dummy_library, library_db, query_start, query_end)
    rmtree.rmtree(library_location, test=True)


@pytest.fixture
def libraries_list(library_root):
    """
    returns a list of libraries loaded
    """
    import os
    
    return(next(os.walk(library_root))[1])


@pytest.fixture(scope="session")
def notebooks_list():
    """
    returns a list of the notebooks loaded in the temp library
    """
    import os

    return(os.listdir(os.path.join('tests', 'test_notebooks')))
