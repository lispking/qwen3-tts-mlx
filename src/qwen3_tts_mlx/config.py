import os
from dataclasses import dataclass
from typing import Optional

# Get the package root directory
PACKAGE_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(PACKAGE_ROOT))

@dataclass
class TTSConfig:
    """TTS configuration class with all default parameters"""

    model: str = "mlx-community/Qwen3-TTS-12Hz-1.7B-Base-5bit"
    text: str = "Hello, this is a test."
    ref_audio: str = os.path.join(PROJECT_ROOT, "tests", "Kai.wav")
    ref_text: Optional[str] = "最近听到的一首歌，这种雷鬼风格，它就真的带给人非常欢快的感觉。"
    lang_code: str = "z"
    output_path: Optional[str] = None
