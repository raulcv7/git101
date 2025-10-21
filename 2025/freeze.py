from app import app, load_snippets
from flask_frozen import Freezer
from pathlib import Path
import shutil

freezer = Freezer(app)

# Snippet pages
@freezer.register_generator
def snippet():
    snippets = load_snippets()
    for s in snippets:
        if 'slug' in s and s['slug']:
            yield {'slug': s['slug']}

# Static files
@freezer.register_generator
def static_files():
    static_folder = Path(app.static_folder)
    for filepath in static_folder.rglob('*'):
        if filepath.is_file():
            rel_path = filepath.relative_to(static_folder)
            yield f'/static/{rel_path}'

if __name__ == "__main__":
    # Clean build folder
    build_path = Path('build')
    if build_path.exists():
        shutil.rmtree(build_path)
    freezer.freeze()
