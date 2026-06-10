from scripts.pipeline import output



def main():

    request = "Comment avoir de bonnes méthodes financières"

    for chunk in output(request):
        print(chunk, end="", flush=True)


if __name__ == "__main__":
    main()
