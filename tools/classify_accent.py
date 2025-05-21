@tool
def classify_accent(audio_path: str) -> dict:
    """Classifies the accent from an English speech audio file and returns the accent and confidence score."""
    
    classifier = EncoderClassifier.from_hparams(
        source="Jzuluaga/accent-id-commonaccent_ecapa",
        savedir="pretrained_models/accent-id-commonaccent_ecapa"
    )
    out_prob, score, index, text_lab = classifier.classify_file(audio_path)

    return {
        "accent": text_lab,
        "confidence": round(float(score), 4)
    }
