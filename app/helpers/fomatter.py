def get_formatted_errors(form):
    error_messages = []
    for field, messages in form.errors.items():
        for message in messages:
            error_messages.append(f"{field}: {message}")

    formatted_errors = "\n".join(error_messages)
    return formatted_errors
