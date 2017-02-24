from jieba.analyse import extract_tags

txt_dir = ['raw_txt/{}.txt'.format(key) for key in range(1, 25)]
result_dir = ['kw_result/{}.txt'.format(key) for key in range(1, 25)]

for i in range(len(txt_dir)):
    with open(txt_dir[i], 'r') as f:
        raw_list = f.readlines()
    raw_list = [txt.strip() for txt in raw_list]
    gb_text = ''.join(raw_list)
    result = extract_tags(gb_text, topK=50)
    with open(result_dir[i], 'w') as wf:
        for kw in result:
            wf.write(kw + '\n')




# if __name__ == '__main__':
#     print(result)