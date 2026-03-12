# Custom exception class for incomplete ledger data
class IncompleteDataError(Exception):
    """Raised when an empty line (incomplete data) is found in the ledger."""
    pass


# Generator function that yields ledger lines
def ledger_reader(lines):
    """
    Generator that processes lines from a financial ledger.
    If an empty line is encountered, raise IncompleteDataError.
    """
    for line_number, line in enumerate(lines, start=1):

        # Remove surrounding whitespace
        clean_line = line.strip()

        # Check for empty line
        if clean_line == "":
            # Raise custom exception with line information
            raise IncompleteDataError(f"Incomplete data at line {line_number}")

        # Yield valid ledger entry
        yield clean_line


# ---------------------------
# Example ledger data
ledger_data = [
    "2026-01-01,Deposit,500",
    "2026-01-02,Withdrawal,200",
    "",   # <-- Problematic empty line
    "2026-01-03,Deposit,300"
]


# ---------------------------
# OPTION 1: Resume processing after handling the error
print("Resuming processing example:")

reader = ledger_reader(ledger_data)

while True:
    try:
        # Get next ledger entry
        entry = next(reader)
        print("Processed:", entry)

    except IncompleteDataError as e:
        # Handle the problem and continue
        print("Warning:", e)
        print("Skipping empty line and resuming...")
        continue

    except StopIteration:
        # Generator finished normally
        print("Finished processing ledger.")
        break


# ---------------------------
# OPTION 2: Safely exit when error occurs
print("\nSafe exit example:")

try:
    for entry in ledger_reader(ledger_data):
        print("Processed:", entry)

except IncompleteDataError as e:
    # Stop processing safely
    print("Error encountered:", e)
    print("Stopping ledger processing safely.")