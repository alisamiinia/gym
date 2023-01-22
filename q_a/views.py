from django.shortcuts import render

from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionSerializer, AnswerSerializer, QuestionScoreSerializer, AnswerScoreSerializer
from .models import QuestionScore, AnswerScore
from django.core import serializers

# Create your views here.


# @api_view(['POST'])
# def post_card(request):        
#     if request.method == "POST":
#         ser = CardSerializer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_question(request):        
    if request.method == "POST":
        ser = QuestionSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def post_answer(request):        
    if request.method == "POST":
        ser = AnswerSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

# def set_question_score(userId, questionId, score):
@api_view(['POST'])
def post_question_score(request):
    if request.method == "POST":
        my_objects = list(QuestionScore.objects.filter(questionId=request.data.get('questionId')))
        tmp = ""
        flag = False
        for question in my_objects:
            if question.userId == request.data.get('userId'):
                tmp = question
                flag = True
        if not flag:
            ser = QuestionScoreSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                s = {
                    "userId": ser.data['userId'],
                    "questionId": ser.data['questionId'],
                    "score": ser.data['score'],
                    "totalScore": Question.objects.get(id=ser.data['questionId']).score()
                }
                return Response(s, status=status.HTTP_201_CREATED)
            else:
                return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        else :
            tmp.score = request.data.get('score')
            tmp.save()
            score_id = tmp.id
            obj = QuestionScore.objects.get(id=score_id)
            content = {
                # "id": score_id,
                "userId": obj.userId,
                "questionId": obj.questionId,
                "score": obj.score,
                "totalScore": Question.objects.get(id=obj.questionId).score()

            }
            return Response(content, status=status.HTTP_200_OK)

    #     ser = QuestionScoreSerializer(data=request.data)
    #     if ser.is_valid():
    #         ser.save()
    #         return Response(ser.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == 'PUT':
    #     score = request.data
    #     score_id = score.get('id', None)
    #     if score_id:
    #         inv_score = QuestionScore.objects.get(id=score_id)
    #         inv_score.score = score.get('score', inv_score.score)
    #         inv_score.save()
    #     else:
    #         tmp = QuestionScore.objects.create(**score)
    #         score_id = tmp.pk

    #     obj = QuestionScore.objects.get(id=score_id)
    #     content = {
    #         "id": score_id,
    #         "userId": obj.userId,
    #         "questionId": obj.questionId,
    #         "score": obj.score
    #     }
    #     return Response(content, status=status.HTTP_200_OK)




@api_view(['POST'])
def post_answer_score(request):
    if request.method == "POST":
        # instance = get_object_or_404(Coach, pk=pk)
        # tmp = get_object_or_404(AnswerScore, answerId = request.data.get('answerId'), userId = request.data.get('userId'))
        my_objects = list(AnswerScore.objects.filter(answerId=request.data.get('answerId')))
        tmp = ""
        flag = False
        for answer in my_objects:
            if answer.userId == request.data.get('userId'):
                tmp = answer
                flag = True
        if not flag:
            ser = AnswerScoreSerializer(data=request.data)
            if ser.is_valid():
                ser.save()
                s = {
                    "userId": ser.data['userId'],
                    "answerId": ser.data['answerId'],
                    "score": ser.data['score'],
                    "totalScore": Answer.objects.get(id=ser.data['answerId']).score()
                }
                return Response(s, status=status.HTTP_201_CREATED)
            else:
                return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        else :
            tmp.score = request.data.get('score')
            tmp.save()
            score_id = tmp.id
            obj = AnswerScore.objects.get(id=score_id)
            content = {
                # "id": score_id,
                "userId": obj.userId,
                "answerId": obj.answerId,
                "score": obj.score,
                "totalScore": Answer.objects.get(id=obj.answerId).score()
            }
            return Response(content, status=status.HTTP_200_OK)


from .models import Question, Answer
@api_view(['GET'])
def get_question(request, questionId, userId):
        question = Question.objects.get(id=questionId)
        answers = Answer.objects.filter(questionId=questionId)
        # ans_ser = AnswerSerializer(answers,many=True)
        qs = QuestionSerializer(question)
        ans_content = []
        for ans in answers:
            ans_ser = AnswerSerializer(ans)
            userScore = 0
            try:
                userScore = AnswerScore.objects.get(answerId=ans.id, userId=userId).score
            except:
                pass
            tmp_content = {
                'answerDetail': ans_ser.data,
                'score': ans.score(),
                'userScore': userScore #AnswerScore.objects.get(answerId=ans.id, userId=userId).score
            }
            
            if question.acceptedAnswerId == ans.id:
                ans_content.insert(0,tmp_content)
            else:
                ans_content.append(tmp_content)
        userScore = 0
        try: 
            userScore = QuestionScore.objects.get(questionId=questionId, userId=userId).score
        except :
            pass
        content = {
        'score': question.score(),
        'userScore': userScore, #QuestionScore.objects.get(questionId=questionId, userId=userId).score,
        'questionDetail' : qs.data, 
        'answerCount': question.answer_count(),
        'Answers': ans_content
        }
        return Response(content, status=status.HTTP_200_OK)
        # return Response(QuestionSerializer(questions,many=True).data,
                    # status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user_questions(request, writerId):
        questions = Question.objects.filter(writerId=writerId)
        content = []
        for question in questions:
            qs = QuestionSerializer(question)
            userScore = 0
            try: 
                userScore = QuestionScore.objects.get(questionId=question.id, userId=writerId).score
            except :
                pass
            tmp_content = {
            'questionDetail' : qs.data, 
            'score': question.score(),
            'userScore': userScore,
            'answerCount': question.answer_count()
            }
            content.append(tmp_content)
        return Response(content, status=status.HTTP_200_OK)
        # return Response(QuestionSerializer(questions,many=True).data,
                    # status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_answers(request, writerId):
        answers = Answer.objects.filter(writerId=writerId)
        content = []
        for answer in answers:
            ans = AnswerSerializer(answer)
            userScore = 0
            try: 
                userScore = AnswerScore.objects.get(answerId=Answer.id, userId=writerId).score
            except :
                pass
            tmp_content = {
                'AnswerDetail' : ans.data, 
                'score': answer.score(),
                'userScore': userScore,
                'questionTitle': Question.objects.get(id = answer.questionId).title
            }
            content.append(tmp_content)
        return Response(content, status=status.HTTP_200_OK)
    
@api_view(['GET'])
def search_questions(request, category, str):    
    questions = Question.objects.filter(category=category)
    content = []
    for question in questions:
        if str not in question.title:
            continue
        qs = QuestionSerializer(question)
        userScore = 0
        try: 
            userScore = QuestionScore.objects.get(questionId=question.id, userId=qs.data['writerId']).score
        except:
            pass
        tmp_content = {
        'questionDetail' : qs.data, 
        'score': question.score(),
        'userScore': userScore,
        'answerCount': question.answer_count()
        }
        content.append(tmp_content)
    return Response(content, status=status.HTTP_200_OK)        
    #tmp = coachs.filter(user__contains='fullName')
    