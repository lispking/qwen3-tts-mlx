# Qwen3 TTS MLX

A simple and easy-to-use wrapper package for Qwen3 TTS based on MLX Audio. This package provides a streamlined interface for text-to-speech synthesis using the Qwen3 TTS model on Apple Silicon devices.

## Features

- 🎯 **Simple API**: Easy-to-use Python API and command-line interface
- ⚙️ **Configurable**: All parameters can be customized with sensible defaults
- 🚀 **MLX Optimized**: Built on Apple's MLX framework for efficient inference on Apple Silicon
- 📦 **Easy Installation**: Install locally with pip

## Requirements

- Python 3.9 or higher
- macOS with Apple Silicon (M1/M2/M3)
- [mlx-audio](https://github.com/Blaizzy/mlx-audio) dependency

## Installation

### From Source

```bash
git clone https://github.com/lispking/qwen3-tts-mlx.git
cd qwen3-tts-mlx
pip install -e .
```

### Install Dependencies

The package requires `mlx-audio` which will be installed automatically:

```bash
pip install mlx-audio
```

## Usage

### Python API

#### Basic Usage

```python
from qwen3_tts_mlx import generate_tts

# Use default configuration
generate_tts()
```

#### Custom Parameters

```python
from qwen3_tts_mlx import generate_tts, TTSConfig

# Method 1: Pass parameters directly
generate_tts(
    text="Hello, welcome to the world of text-to-speech!",
    lang_code="en",
)

# Method 2: Use configuration object
config = TTSConfig(
    text="你好，欢迎使用语音合成！",
    lang_code="zh",
    ref_audio="path/to/your/reference.wav"
)
generate_tts(
    text=config.text,
    lang_code=config.lang_code,
    ref_audio=config.ref_audio,
)
```

#### Advanced Usage

```python
from qwen3_tts_mlx import generate_tts

# Full parameter customization
generate_tts(
    model="mlx-community/Qwen3-TTS-12Hz-1.7B-Base-5bit",
    text="Your text here",
    ref_audio="tests/Kai.wav",
    ref_text="Reference text for the audio",
    lang_code="en",
)
```

#### Custom Output Path

```python
from qwen3_tts_mlx import generate_tts

# Save to specific file
output_file = generate_tts(
    text="Hello World",
    output_path="output/my_audio.wav"
)
print(f"Audio saved to: {output_file}")

# Save to directory with auto-generated filename
output_file = generate_tts(
    text="Hello World",
    output_path="output/"
)
```

### Command Line Tool

#### Basic Usage

```bash
# Use default configuration
qwen3-tts-mlx
```

#### Custom Parameters

```bash
# Specify text and language
qwen3-tts-mlx --text "Hello World" --lang-code en

# Use custom reference audio
qwen3-tts-mlx --text "Your text" --ref-audio "path/to/audio.wav"

# Use different model
qwen3-tts-mlx --model "mlx-community/Qwen3-TTS-12Hz-1.7B-Base-5bit" --text "Hello"

# Save to custom output path
qwen3-tts-mlx --text "Hello World" --output "output/my_audio.wav"
```

#### View All Options

```bash
qwen3-tts-mlx --help
```

Output:
```
usage: qwen3-tts-mlx [-h] [--model MODEL] [--text TEXT] [--ref-audio REF_AUDIO]
                     [--ref-text REF_TEXT] [--lang-code LANG_CODE] [--output OUTPUT]

Qwen3 TTS MLX Command Line Tool

options:
  -h, --help            show this help message and exit
  --model MODEL         Model name or path (default: mlx-community/Qwen3-TTS-12Hz-1.7B-Base-5bit)
  --text TEXT           Text to convert (default: "Hello, this is a test.")
  --ref-audio REF_AUDIO
                        Reference audio path (default: tests/Kai.wav)
  --ref-text REF_TEXT   Reference text (default: None)
  --lang-code LANG_CODE
                        Language code (default: z)
  --output OUTPUT       Output audio file path (default: audio_000.wav in current directory)
```

## Configuration Parameters

| Parameter | Default Value | Description |
|-----------|---------------|-------------|
| `model` | `mlx-community/Qwen3-TTS-12Hz-1.7B-Base-5bit` | Model name or path from HuggingFace |
| `text` | `Hello, this is a test.` | Text to convert to speech |
| `ref_audio` | `tests/Kai.wav` | Reference audio file path for voice cloning |
| `ref_text` | `None` | Reference text corresponding to the reference audio |
| `lang_code` | `z` | Language code (e.g., 'en', 'zh', 'z') |
| `output_path` | `None` | Output audio file path (default: `audio_000.wav` in current directory) |

### Language Codes

Common language codes supported:
- `en` - English
- `zh` - Chinese
- `z` - Auto-detect or default

## Project Structure

```
qwen3-tts-mlx/
├── src/
│   └── qwen3_tts_mlx/
│       ├── __init__.py      # Package initialization
│       ├── config.py        # Configuration class with defaults
│       ├── tts.py           # Core TTS functionality
│       └── cli.py           # Command-line interface
├── tests/                   # Reference audio directory
│   └── .gitkeep
├── pyproject.toml           # Package configuration
├── LICENSE                  # Apache 2.0 License
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/lispking/qwen3-tts-mlx.git
cd qwen3-tts-mlx

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

## Model Information

This package uses the Qwen3 TTS model from the MLX Community:

- **Model**: `mlx-community/Qwen3-TTS-12Hz-1.7B-Base-5bit`
- **Size**: 1.7B parameters (5-bit quantized)
- **Framework**: MLX (Apple Machine Learning framework)
- **Hardware**: Optimized for Apple Silicon (M1/M2/M3)

The model will be downloaded automatically on first use.

## Reference Audio

Place your reference audio files in the `tests/` directory. The default reference audio is expected at `tests/Kai.wav`.

Supported audio formats:
- WAV
- MP3
- FLAC

## Troubleshooting

### Common Issues

1. **Model download fails**
   - Check your internet connection
   - Ensure you have enough disk space

2. **Reference audio not found**
   - Place your audio file in the `tests/` directory
   - Or specify the full path with `--ref-audio`

3. **MLX not available**
   - Ensure you're running on macOS with Apple Silicon
   - Install mlx: `pip install mlx`

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [MLX Audio](https://github.com/Blaizzy/mlx-audio) - The underlying TTS framework
- [Qwen3 TTS](https://huggingface.co/mlx-community/Qwen3-TTS-12Hz-1.7B-Base-5bit) - The TTS model by MLX Community
- [Apple MLX](https://github.com/ml-explore/mlx) - Machine learning framework for Apple Silicon

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on the repository.
