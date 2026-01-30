import os
from typing import Optional

from mlx_audio.tts.utils import load_model
from mlx_audio.tts.generate import generate_audio

from .config import TTSConfig


def generate_tts(
    model: Optional[str] = None,
    text: Optional[str] = None,
    ref_audio: Optional[str] = None,
    ref_text: Optional[str] = None,
    lang_code: Optional[str] = None,
    output_path: Optional[str] = None,
) -> str:
    """
    Generate TTS audio

    Args:
        model: Model name or path, defaults to TTSConfig.model
        text: Text to convert, defaults to TTSConfig.text
        ref_audio: Reference audio path, defaults to TTSConfig.ref_audio
        ref_text: Reference text, defaults to TTSConfig.ref_text
        lang_code: Language code, defaults to TTSConfig.lang_code
        output_path: Output audio file path, defaults to current directory

    Returns:
        Path to the generated audio file
    """
    config = TTSConfig()

    model = model or config.model
    text = text or config.text
    ref_audio = ref_audio or config.ref_audio
    ref_text = ref_text or config.ref_text
    lang_code = lang_code or config.lang_code
    output_path = output_path or config.output_path

    loaded_model = load_model(model)

    # Parse output_path into directory and filename prefix
    output_dir = None
    file_prefix = "audio"
    if output_path:
        output_dir = os.path.dirname(output_path)
        base_name = os.path.basename(output_path)
        # Remove extension if present
        if base_name:
            file_prefix = os.path.splitext(base_name)[0] or "audio"
        
        # Create output directory if it doesn't exist
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir, exist_ok=True)
    
    # Change to output directory if specified
    original_dir = None
    if output_dir:
        original_dir = os.getcwd()
        os.chdir(output_dir)

    generated_file = f"{file_prefix}_000.wav"
    target_file = f"{file_prefix}.wav"
    
    try:
        generate_audio(
            model=loaded_model,
            text=text,
            ref_audio=ref_audio,
            ref_text=ref_text,
            lang_code=lang_code,
            file_prefix=file_prefix,
        )
        
        # Rename file to remove _000 suffix
        if os.path.exists(generated_file) and generated_file != target_file:
            os.rename(generated_file, target_file)
    finally:
        # Restore original directory
        if original_dir:
            os.chdir(original_dir)

    # Return the actual output path
    return os.path.join(output_dir or ".", target_file)
