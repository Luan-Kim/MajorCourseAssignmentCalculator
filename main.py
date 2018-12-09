"""
대덕소프웨어마이스터고등학교 전공심화과정 배치 점수 산출기
Major Course Assignment Score Calculator for Daedeok Software Meister High School
Copyright (c) 2018 Suhyuk Park

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import datetime

# Define variables.
dept_full = ["SW개발과", "임베디드SW과", "정보보안과"]
dept_simple = ["가", "나", "다"]
subject_list = [["국어", "수학", "영어", "통합사회", "통합과학", "체육", "음악", "컴퓨터 구조", "프로그래밍"],
                ["국어", "수학", "영어", "통합사회", "통합과학", "체육", "음악", "자료구조와 알고리즘", "C++ 프로그래밍"]]
certificate_list = ["인문", "인성", "외국어", "예체능", "전문"]

number, name, parent, yr, cls, nbr = 0, 0, 0, 0, 0, 0
major = list()


def response(string="계속하려면 아무 키나 누르십시오..."):
    return input(string)


def warning():
    print("알림: 이 소프트웨어는 개인 프로젝트이며, 대덕소프트웨어마이스터고등학교로부터 어떠한 인가도 받지 않았습니다.\n\n")

    
def report(string, custom=False, score=0):
    print("-" * 55)
    print("\t\t{}".format(string))
    print("\t1학년 ( {} ) 반 ( {} ) 번".format(cls, nbr))
    print("\t학 생 : {} (인)\t학부모 : {} (인)".format(name, parent))
    print("\t" + "*" * 40)
    print("\t1학년\t배정과정\t희망 순위")
    print("\t" + "*" * 40)
    print("\t\t\tSW개발과\t{}".format(major[0]))
    print("\t공통과정\t임베디드SW과\t{}".format(major[1]))
    print("\t\t\t정보보안과\t{}".format(major[2]))
    if custom:
        print("\t" + "*" * 40)
        print("\t최종점수: {}".format(score))
    print("\n\t대덕소프트웨어마이스터고등학교장")
    print("-" * 55)
    
    
def info():
    print("\t- {}학년도 전공심화과정 배정 안내 -\n".format(datetime.datetime.now().year))
    print("1. 전공심화과정 배정 목적\n",
          "\t가. 전공공통과정을 통해 자신의 적성에 맞는 전공심화과정을 선택할 수 있도록 유도\n",
          '\t나. 전공심화과정 운영을 통한 학교 교육만족도 제고\n')

    print("2. 전공심화과정 배정 계획\n",
          '\t가. 희망 전공과정별로 1학년 성적 및 학교장인증점수 합산 후 득점이 높은 학생 순으로 학과 배정\n')

    print('3. 전공심화과정 내용 및 배정 인원\n',
          "\t[1학년\t\t2학년\t3학년]\n\t[(공통과정)\t (심화과정)]\n",
          "\t가. SW개발과: 학급당 배정인원 20명씩 2개 반\n",
          "\t나. 임베디드SW과: 학급당 배정인원 20명씩 1개 반\n",
          "\t다. 정보보안과: 학급당 배정인원 20명씩 1개 반\n")


def assign():
    global number, name, parent, yr, cls, nbr

    print("학과배정을 시작합니다.")
    while True:
        try:
            value = input("본인의 학번이름과 부모님 성함을 입력해주세요 (예:1214 홍길동 홍판서): ").split()
            number, name, parent = value[0], value[1], value[2]
            yr, cls, nbr = number[0], number[1], number[2:]

            value = input("본인의 지망 과를 희망순위대로 입력해주세요. (가: SW개발과, 나: 임베디드SW과, 다: 정보보안과): ").split()
            for i in value:
                if i not in (dept_full + dept_simple):
                    raise IndexError

            if (value[0] or value[1] or value[2]) in dept_simple:
                is_simplified = True
            else:
                is_simplified = False

            if is_simplified:
                for i in dept_simple:
                    major.append(value.index(i) + 1)
            else:
                for i in dept_full:
                    major.append(value.index(i) + 1)
            break
        except:
            print("값이 이상합니다.\n")

    report("전공과정 배정 희망 신청서")


def get_subject(semester=2):
    print("1학년 교과성적 산출을 시작합니다!\n")
    print("교과성적은 개인의 학기별 과목별 성취수준에 따른 환산점수의 총합입니다.")
    print("자신이 해당 학기에 이수하였던 모든 과목(예체능 포함)의 ABCDE 개수를 \"정확히\" 입력해주세요.\n만약 해당 성취도를 받지 않았으면 0이라고 입력하시면 됩니다. Enter 키를 "
          "누르셔도 0으로 간주합니다.\n")

    value = True
    sch_grade, sch_semester = 0, 0
    while value:
        school = list()
        for i in range(semester):
            if sch_semester >= 2:
                sch_semester = 0
            sch_semester += 1

            if (i + 1) % 2 == 1:  # If grade has changed.
                sch_grade += 1

            print("[{0}학년 {1}학기 교과성적 산출]".format(sch_grade, sch_semester))
            print("이수 과목: {}".format(subject_list[sch_semester - 1]))
            grade = list()
            for j in ("A", "B", "C", "D", "E"):
                try:
                    tmp = int(input("{0}학년 {1}학기에 받은 \"{2}\" 개수: ".format(sch_grade, sch_semester, j)))
                except:
                    tmp = 0
                grade.append(tmp)
            school.append(grade)

        answer = input("지금까지 입력하셨던 내용이 정확한가요? ('예'나 'y'를 눌러주세요): ")
        if answer in ("예", "y", "Y", "yes"):
            value = False
            # Calculate subject grade
            rate = (5, 4, 3, 2, 1)
            learned, converted = list(), list()
            for i in school:
                s, n, hap = 0, 0, 0
                for j in i:
                    n += j
                    s += j * rate[hap]
                    hap += 1
                learned.append(n)
                converted.append(s)

            return learned, converted
        else:
            print("내용이 초기화되었습니다. 다시 입력해주세요.")
            sch_grade, sch_semester = 0, 0


def get_certificate_score():
    print("\n학교장인증제 점수 산출을 시작합니다!\n")
    print("학교장인증제의 모든 영역을 반영합니다. 합산 최고 점수는 250점이며, 영역별 최고점은 50점입니다.")
    print("자신의 인증제 점수를 영역별로 \"정확히\" 입력해주세요.\n만약 해당 사항이 없으면 0이라고 입력하시면 됩니다.\n")

    value = True
    score = list()
    while value:
        switch = True
        score = list()
        try:
            for i in certificate_list:
                score.append(input("\"{} 영역\" 점수: ".format(i)))
        except:
            print("오류: 문제가 생겼습니다. 다시 입력해주세요.")
            switch = False
        if switch:
            try:
                reload = False
                for i in score:
                    if int(i) > 50:
                        reload = True
                if reload:
                    print("값이 이상합니다. 다시 입력해주세요.")
                    continue

                answer = input("지금까지 입력하셨던 내용이 정확한가요? ('예'나 'y'를 눌러주세요): ")
                if answer in ("예", "y", "Y", "yes"):
                    value = False
                    tmp = 0
                    for i in score:
                        tmp += int(i)
                    return tmp
                else:
                    print("내용이 초기화되었습니다. 다시 입력해주세요.")
                    continue
            except:
                print("오류: 엔터 키로는 0 입력이 불가합니다. 다시 입력해주세요.")
                continue


def calculate():
    learned, converted = get_subject()
    subject, calculated = 0, 0
    for i in learned:
        subject += i
    for i in converted:
        calculated += i

    certified = get_certificate_score()
    score = round((calculated / subject * 20 * 0.7) + (certified * 2 / 5 * 0.3), 2)

    report("전공과정 배정 점수 산출표", custom=True, score=score)
 

def main():
    warning()
    info()
    assign()
    calculate()


if __name__ == "__main__":
    main()
