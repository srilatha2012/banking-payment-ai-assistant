from assistant_service import get_answer


while True:
    return_code = input(
        "\nEnter ACH return code (or 'exit' to quit): "
    ).strip()

    if return_code.upper() == "EXIT":
        print("Goodbye!")
        break

    answer = get_answer(return_code)
    print(answer)