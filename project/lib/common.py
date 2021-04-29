
def try_except(fun):
    def handling(*args, **kwargs):
        try:
            fun(*args, **kwargs)
        except FileNotFoundError as e:
            print(f"File not found.\n{e}")
        except FileExistsError as e:
            print(f"File already exists\n{e}")
        except PermissionError as e:
            print(f"permission dennied for the file.\n{e}")
        except Exception as e:
            print(e)
    return handling