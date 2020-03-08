# -*- coding: utf-8 -*- 
'''
* 실험 전에 result.txt 빈 파일 생성하고 시작
1. profile 결과 생성
: sudo profile/profile --s 256m mem.msys >> myprof.res
2. 실험 번호 출력 (예시: #1)
3. 실험 결과를 출력
4. 한줄 띄어쓰기
5. 프로파일 결과 삭제 
'''

import sys
import os
import argparse

def main(cnt):
#	comp0='echo 20190305 | sudo -S profile/profile --s 256m mem.msys >> myprof.res'
#	comp1='echo 20190305 | sudo -S profile/profile --s 512m mem.msys >> myprof1.res'
	comp2='echo 20190305 | sudo -S profile/profile --s 1024m mem.msys >> myprof2.res'
#	comp3='echo 20190305 | sudo -S profile/profile --s 2048m mem.msys >> myprof.res'
	delcomp='rm myprof.res'
#	attcomp0='py/ffs_exploit.py myprof.res mem.msys >> result0.txt'
#	attcomp1='py/ffs_exploit.py myprof1.res mem.msys >> result1.txt'
	attcomp2='py/ffs_exploit.py myprof2.res mem.msys >> result2.txt'
#	attcomp3='py/ffs_exploit.py myprof.res mem.msys >> result3.txt'

#	f = open(res, 'w')
	count=int(cnt)
	for i in range(count):
		'''
		os.system(comp0)
		print("profile0 파일 생성 완료.\n")
		os.system(attcomp0)
		os.system(delcomp)
		print("%d번째 실험 완료.\n" % (i+1))
		
		os.system(comp1)
		print("profile1 파일 생성 완료.\n")	
		os.system(attcomp1)
		#os.system(delcomp)
		print("%d번째 실험 완료.\n" % (i+1))
'''
		os.system(comp2)
		print("profile2 파일 생성 완료.\n") 
		os.system(attcomp2)
#		os.system(delcomp)
		print("%d번째 실험 완료.\n" % (i+1))
'''	
		os.system(comp3)
		print("profile3 파일 생성 완료.\n")
		os.system(attcomp3)
		os.system(delcomp)
		print("%d번째 실험 완료.\n" % (i+1))
'''

	#f.close()		

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Rowhammer simulation(Flip Feng Shui ver.)')
#	parser.add_argument("--result_text_path", help=" ")
	parser.add_argument("--experiment_count", help=" ")
	args = parser.parse_args()
#	res = args.result_text_path
	cnt = args.experiment_count
	main(cnt)

