# Code Cartographer

This project provides a Gradio-based web interface for extracting and processing archive files. It supports various archive formats including ZIP, RAR, and 7z. The tool extracts the contents of the uploaded archive, generates a directory tree, and displays the contents of text files while respecting .gitignore patterns and common ignore rules.

## Features

- Support for ZIP, RAR, and other archive formats (via py7zr)
- Respects .gitignore patterns if present in the archive
- Ignores common cache and system files
- Generates a visual directory tree
- Displays contents of text files
- Provides a user-friendly web interface

## AI Integration and Context Provision

This File Extractor and Processor is particularly valuable when working with AI systems, especially Large Language Models (LLMs). Here's how it can enhance your AI-assisted development and analysis workflows:

1. **Project Context for Code Understanding**: By extracting and presenting the entire structure and content of a project, you can provide comprehensive context to an AI. This allows the AI to better understand the project's architecture, dependencies, and overall codebase, leading to more accurate and relevant assistance.

2. **Efficient Code Reviews**: When reviewing large projects or pull requests, you can use this tool to quickly extract and summarize changes. The extracted information can then be fed to an AI for rapid analysis, helping to identify potential issues or improvements.

3. **Documentation Generation**: The extracted project structure and file contents can serve as input for AI-powered documentation generators. This can help in creating or updating README files, API documentation, or even generating code comments.

4. **Dependency Analysis**: By presenting the full project structure, including requirements files, an AI can more accurately analyze and suggest updates or alternatives for project dependencies.

5. **Code Refactoring Suggestions**: With a complete view of the project, an AI can provide more contextually aware suggestions for code refactoring, taking into account the entire project structure and interdependencies.

6. **Troubleshooting and Debugging**: When facing issues, you can extract relevant parts of your project and present them to an AI for analysis. This comprehensive view can help in identifying potential sources of bugs or conflicts.

7. **Learning and Training**: For developers learning new frameworks or languages, this tool can help in extracting and presenting example projects to an AI, which can then provide explanations and insights about the project structure and coding patterns.

8. **Consistent Style Enforcement**: By providing the full project context, an AI can offer suggestions to maintain consistent coding style and practices across the entire codebase.

9. **Security Audits**: The comprehensive project view allows AI systems to perform more thorough security analyses, identifying potential vulnerabilities in the context of the entire application.

10. **Integration with AI-Powered IDEs**: The output from this tool can be seamlessly integrated with AI-powered development environments, providing them with richer context for more accurate code completion, refactoring suggestions, and error detection.

To use this tool with an AI system:

1. Extract your project using the File Extractor and Processor.
2. Copy the output using the "Copy to Clipboard" button.
3. Paste the extracted information into your conversation with the AI, providing it with comprehensive project context.
4. Ask your questions or request analysis based on this context.

This approach ensures that the AI has a full understanding of your project's structure and contents, leading to more accurate and contextually relevant assistance.


## Requirements

This project requires Python 3.6 or higher. All required packages are listed in the `requirements.txt` file. You can install them using pip:

```
pip install -r requirements.txt
```

Make sure you have the following packages installed:

- gradio
- rarfile
- py7zr
- pathspec

Note: For RAR file support, you need to have the `unrar` command-line tool installed on your system. If it's not available, the script will fall back to using py7zr for RAR files.

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/file-extractor-processor.git
   cd file-extractor-processor
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```
   python file_extractor_processor.py
   ```

2. Open your web browser and go to the URL displayed in the console (usually `http://127.0.0.1:7860`).

3. Upload an archive file using the file upload input.

4. Click the "Extract and Process" button.

5. View the extracted contents, directory structure, and file contents in the output text area.

6. Use the "Copy to Clipboard" button to copy the entire output.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](https://github.com/dryruffian/CodeCartographerUI/blob/main/LICENSE.md).
