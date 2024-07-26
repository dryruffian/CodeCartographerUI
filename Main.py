import os
import zipfile
import rarfile
import py7zr
import gradio as gr
import pathspec
import shutil

# Default ignore patterns (same as before)
DEFAULT_IGNORE_PATTERNS = [
    '.git', '.gitignore', '.gitattributes', '.gitmodules',
    '__pycache__', '*.pyc', '*.pyo', '*.pyd',
    'node_modules', 'npm-debug.log',
    '.DS_Store',
    '.vscode', '.idea', '*.swp',
    '*.class', '*.o', '*.so',
    '*.log',
    '*~', '*.bak', '*.tmp',
]

def extract_file(file_path, extract_dir):
    file_lower = file_path.lower()
    if file_lower.endswith('.zip'):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
    elif file_lower.endswith('.rar'):
        try:
            with rarfile.RarFile(file_path, 'r') as rar_ref:
                rar_ref.extractall(extract_dir)
        except rarfile.RarCannotExec:
            # If unrar is not installed, try py7zr as a fallback
            with py7zr.SevenZipFile(file_path, mode='r') as z:
                z.extractall(path=extract_dir)
    else:
        # Try py7zr for other formats
        with py7zr.SevenZipFile(file_path, mode='r') as z:
            z.extractall(path=extract_dir)

def extract_and_process(file):
    temp_dir = "temp_extracted"
    os.makedirs(temp_dir, exist_ok=True)
    
    try:
        extract_file(file.name, temp_dir)
    except Exception as e:
        shutil.rmtree(temp_dir)
        return f"Error extracting file: {str(e)}. Please ensure it's a valid archive file."

    gitignore = os.path.join(temp_dir, '.gitignore')
    if os.path.exists(gitignore):
        with open(gitignore, 'r') as f:
            ignore_patterns = f.read().splitlines() + DEFAULT_IGNORE_PATTERNS
    else:
        ignore_patterns = DEFAULT_IGNORE_PATTERNS

    spec = pathspec.PathSpec.from_lines('gitwildmatch', ignore_patterns)

    tree = generate_tree(temp_dir, spec)
    output = tree + "\n\n"
    output += process_directory(temp_dir, spec)
    
    shutil.rmtree(temp_dir)
    
    return output

def generate_tree(path, spec):
    tree = "Working Directory Tree:\n"
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        root_name = os.path.basename(root)
        if not spec.match_file(os.path.relpath(root, path)):
            tree += f"{indent}{root_name}/\n"
            sub_indent = ' ' * 4 * (level + 1)
            for file in files:
                file_path = os.path.relpath(os.path.join(root, file), path)
                if not spec.match_file(file_path):
                    tree += f"{sub_indent}{file}\n"
        dirs[:] = [d for d in dirs if not spec.match_file(os.path.relpath(os.path.join(root, d), path))]
    return tree

def process_directory(path, spec):
    output = ""
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, path)
            if not spec.match_file(relative_path):
                output += f"#{relative_path}\n"
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        output += f.read() + "\n\n"
                except UnicodeDecodeError:
                    output += f"[Binary file contents not shown]\n\n"
        dirs[:] = [d for d in dirs if not spec.match_file(os.path.relpath(os.path.join(root, d), path))]
    return output

# JavaScript function to copy text to clipboard
js_copy = """
function copyToClipboard() {
    var textArea = document.querySelector('.output-text textarea');
    textArea.select();
    document.execCommand('copy');
}
"""

with gr.Blocks(css="#copy_button { margin-top: 10px; }") as iface:
    gr.Markdown("# File Extractor and Processor")
    gr.Markdown("Upload an archive file to extract its contents and view the directory structure and file contents. Respects .gitignore if present and ignores common cache and system files.")
    
    with gr.Row():
        input_file = gr.File(label="Upload archive file (ZIP, RAR, or other supported formats)")
    
    with gr.Row():
        output = gr.Textbox(label="Extracted Content", lines=25, elem_classes=["output-text"])
    
    with gr.Row():
        submit_button = gr.Button("Extract and Process")
        copy_button = gr.Button("Copy to Clipboard", elem_id="copy_button")

    submit_button.click(extract_and_process, inputs=input_file, outputs=output)
    copy_button.click(None, [], [],js=js_copy)

iface.launch()