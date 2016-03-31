import sys, os

def generate(csv):
	output = '#EXTM3U\r\n\r\n'

	with open(csv, 'r') as lines:
		
		count = 0
	
		for line in lines:
			line = line.rstrip()

			if count > 0:
				info = line.split(',')

				formatted = ''

				if len(info) == 4:
					if info[0] == '' and info[1] == '' and info[2] == '' and info[3] == '':
						formatted = '\r\n\r\n'
					else:
						formatted = '#EXTINF:-1,%s - [%03d] %s\r\n' % (
							info[0], int(info[1]), info[2]
						)

						formatted += 'rtp://@%s\r\n\r\n' % info[3]

				output += formatted

			count += 1

	return output

if __name__ == '__main__':
	if len(sys.argv) is not 3:
		print('\nInvalid arguments!\n')
		print('Usage:\n >> %s <source.csv> <destination.m3u>\n' % sys.argv[0])
		print('Example:\n >> %s database/channels.csv playlist.m3u\n' % sys.argv[0])
	
	else:
		src = sys.argv[1]
		dst = sys.argv[2]

		if not os.path.isfile(src):
			print('ERROR: Source file \'%s\' is not exist!' % src)
		else:
			output = generate(src)
			
			try:
				f = open(dst, 'w')
				f.write(output)
			except Exception as e:
				print('Exception: %s\n' % e)