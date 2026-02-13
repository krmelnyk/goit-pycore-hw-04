def add_contact(args, contacts):
    """Add a new contact to the phone book."""
    if len(args) != 2:
        return "Invalid command format."
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """Update an existing contact phone number."""
    if len(args) != 2:
        return "Invalid command format."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."


def show_phone(args, contacts):
    """Return the phone number for a given contact name."""
    if len(args) != 1:
        return "Invalid command format."
    return contacts.get(args[0], "Contact not found.")


def show_all(contacts):
    """Return all saved contacts as a formatted multi-line string."""
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
