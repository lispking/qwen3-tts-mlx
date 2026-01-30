import argparse
from .tts import generate_tts


def main():
    parser = argparse.ArgumentParser(description="Qwen3 TTS MLX Command Line Tool")
    parser.add_argument(
        "--model",
        type=str,
        default=None,
        help='Model name or path (default: mlx-community/Qwen3-TTS-12Hz-1.7B-Base-5bit)',
    )
    parser.add_argument(
        "--text",
        type=str,
        default=None,
        help='Text to convert (default: "Hello, this is a test.")',
    )
    parser.add_argument(
        "--ref-audio",
        type=str,
        default=None,
        help='Reference audio path (default: tests/Kai.wav)',
    )
    parser.add_argument(
        "--ref-text",
        type=str,
        default=None,
        help='Reference text (default: None)',
    )
    parser.add_argument(
        "--lang-code",
        type=str,
        default=None,
        help='Language code (default: z)',
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help='Output audio file path (default: audio_000.wav in current directory)',
    )
    parser.add_argument(
        "--speed",
        type=float,
        default=None,
        help='Speech speed multiplier (default: 1.0)',
    )

    args = parser.parse_args()

    generate_tts(
        model=args.model,
        text=args.text,
        ref_audio=args.ref_audio,
        ref_text=args.ref_text,
        lang_code=args.lang_code,
        output_path=args.output,
        speed=args.speed,
    )


if __name__ == "__main__":
    main()
