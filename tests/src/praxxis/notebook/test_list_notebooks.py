"""
tests listing notebooks
"""
import pytest 


from tests.src.praxxis.fixtures.setup_library import add_test_library

def test_list_notebooks_empty(setup, library_db, current_scene_db, query_start, query_end):
    """ tests listing notebooks when no libraries exist """
    import os
    from src.praxxis.notebook import list_notebook
    from src.praxxis.scene import current_scene
    notebooks = list_notebook.list_notebook(library_db, current_scene_db, query_start, query_end)
    assert notebooks == []


def test_list_notebooks_populated(setup, add_test_library, library_db, current_scene_db, query_start, query_end, notebooks_list):
    from src.praxxis.notebook import list_notebook
    
    notebooks = list_notebook.list_notebook(library_db, current_scene_db, query_start, query_end)
    assert len(notebooks) == len(notebooks_list)