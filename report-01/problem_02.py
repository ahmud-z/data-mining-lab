def student(**params):
    print("Names of all parameters with their values:")
    for key in params.keys():
        print(f"{key} = {params[key]}")


student(name="Ahmud", age=23, dept="CSE")