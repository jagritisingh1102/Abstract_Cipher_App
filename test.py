from abs_cipher import encrypt_func


def test_encrypt_func():
    output1 = encrypt_func("Hello World!")
    print(output1)
    assert output1 == "Svool Dliow!"
    output2 = encrypt_func("Christmas is the 25th of December")
    print(output2)
    assert output2 == "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
