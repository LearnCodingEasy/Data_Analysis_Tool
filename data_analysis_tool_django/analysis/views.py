# from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
import pandas as pd


class SalesDataAPIView(APIView):
    def get(self, request):
        data = {
            'User_Name': ['Ahmed', 'Mahmoud', 'Fatima', 'Sara', 'Hossam'],
            'User_Age': [23, 25, 22, 30, 33],
            'User_Sales': [1200, 1500, 800, 1800, 2500]
        }

        df = pd.DataFrame(data)
        avg_sales = df['User_Sales'].mean()

        response_data = {
            'users': df.to_dict(orient='records'),
            'average_sales': avg_sales
        }

        return Response(response_data)
