import click
from concurrent.futures import ThreadPoolExecutor

write_list = []


def read_file(fin):
    with open(fin, "r") as f_in:
        content = f_in.readlines()
    return content


def write_file(fout, content):
    print("Writing file...")
    with open(fout, "w") as f_out:
        f_out.write(content)
    print(f"File created: {fout}")
    return "File created"


def encrypt_func(content):
    order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse = 'zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA'
    dictChars = dict(zip(order, reverse))
    curr_res = []
    for item in content:
        if item == ' ':
            write_list.append('@')
            curr_res.append('@')
        elif item not in dictChars.keys():
            write_list.append(item)
            curr_res.append(item)
        else:
            write_list.append(dictChars[item])
            curr_res.append(dictChars[item])
    return ''.join(curr_res).replace('@', ' ')


@click.command()
@click.argument('input', type=click.Path(exists=True))
@click.argument('output', type=click.Path())
def main(input, output):
    print(len(read_file(input)))

    with ThreadPoolExecutor(max_workers=len(read_file(input))) as executor:
        executor.map(encrypt_func, read_file(input))
    new_res = "".join(write_list).replace('@', ' ')
    write_file(fout=output, content=new_res)


if __name__ == '__main__':
    main()
