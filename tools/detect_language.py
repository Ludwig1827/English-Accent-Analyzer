@tool
def detect_language_with_confidence(text: str) -> dict:
    """Detects the most likely language of the input text and returns its confidence score."""
    
    detector = LanguageDetectorBuilder.from_all_languages().build()

    # Detect the most likely language
    detected_language = detector.detect_language_of(text)
    detected_language_name = detected_language.name

    # Get all confidence values
    confidence_values = detector.compute_language_confidence_values(text)

    # Find the confidence score for the detected language
    confidence_score = None
    for confidence in confidence_values:
        if confidence.language == detected_language:
            confidence_score = round(confidence.value, 4)
            break

    return {
        "language": detected_language_name,
        "confidence": confidence_score
    }
