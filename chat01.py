#對話紀錄1 - 格式改寫

# step 1: 讀取檔案function
def read_file(filename):
	lines = [] #建立空清單'lines'
	with open (filename, 'r', encoding='utf-8-sig') as f: #打開檔案(此例為input.txt), 讀取模式'r'
								# 'utf-8-sig'後面的-sig, 是為了把文字檔中的字元格式設定值消除, 
								# 若不加此段, 讀取時就會出現'\ufeff'這個亂碼
		for line in f:
			lines.append(line.strip()) #將檔案(此例為input.txt)裡頭的每一行加入lines的最後端
							# .strip()指令: 將換行符號'/n'消除
	return lines #回到lines繼續加

# step 2: 轉換程式function
def convert(lines):
	new = [] #建立新的空清單'new'
	person = None #首先須定義person這個變數, 以防萬一讀取檔案第一行沒有人名, 會當掉
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person: #當person不等於None(也就是person = 'Allen'或'Tom')時
			new.append(person + ': ' + line) #將person與對話內容, 用冒號連接起來, 就完成了
	return new #回傳 new清單

# step 3: 寫入檔案function
def write_file(filename, lines): #投幣孔有兩處: filename & lines
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n') #加上換行符號

# 主程式碼 main:
def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines)

#程式進入點 (呼叫main)
main() 
