from django.db.models import Avg
from django.db.models.functions import TruncDate
from django.shortcuts import render
import datetime
from abc import ABC, abstractmethod

from .models import Dream


class ChartTypeCreator(ABC):
    @abstractmethod
    def create_chart_month(self, request, month, year):
        pass

    @abstractmethod
    def create_chart_week(self, request, week):
        pass


class StressChartCreator(ChartTypeCreator):
    def create_chart_month(self, request, month, year=2023):
        user = request.user.username

        if month == "all":
            data = Dream.objects.filter(user=user).annotate(date=TruncDate('created')).values('created').annotate(
                stres=Avg('stres')).order_by('created')
        elif month == "current":
            current_month = datetime.datetime.now().month
            current_year = datetime.datetime.now().year
            data = Dream.objects.filter(user=user, created__month=current_month, created__year=current_year).annotate(
                date=TruncDate('created')).values('created').annotate(stres=Avg('stres')).order_by('created')
        else:
            if month is not None:
                data = Dream.objects.filter(user=user, created__month=month, created__year=2023).annotate(
                    date=TruncDate('created')).values('created').annotate(stres=Avg('stres')).order_by('created')

        stress_data = []
        date_labels = []
        for item in data:
            stress_data.append(float(item['stres']))
            date_labels.append(item['created'].strftime('%Y-%m-%d'))

        chart_data = {
            'labels': date_labels,
            'datasets': [{
                'label': 'Stress Chart',
                'data': stress_data,
                'fill': 'false',
                'borderColor': 'rgb(0, 0, 0)',
                'lineTension': 0.1
            }]
        }
        return render(request, 'stres_chart.html', {'chart_data': chart_data})

    def create_chart_week(self, request, week):
        user = request.user.username
        data = Dream.objects.filter(user=user)
        if week is not None:
            if week != "all" and week != "current":
                data = data.filter(created__week=week)
            if week == "current":
                today = datetime.date.today()
                current_year, current_week_num, _ = today.isocalendar()
                data = data.filter(created__year=current_year, created__week=current_week_num)
        data = data.annotate(date=TruncDate('created')).values('created').annotate(stres=Avg('stres')).order_by(
            'created')
        stress_data = []
        date_labels = []
        for item in data:
            stress_data.append(float(item['stres']))
            date_labels.append(item['created'].strftime('%Y-%m-%d'))

        chart_data = {
            'labels': date_labels,
            'datasets': [{
                'label': 'Stress Chart',
                'data': stress_data,
                'fill': 'false',
                'borderColor': 'rgb(0, 0, 0)',
                'lineTension': 0.1
            }]
        }
        return render(request, 'stres_chart.html', {'chart_data': chart_data})


class EnergyChartCreator(ChartTypeCreator):
    def create_chart_month(self, request, month, year=2023):
        user = request.user.username

        if month == "all":
            data = Dream.objects.filter(user=user).annotate(date=TruncDate('created')).values('created').annotate(
                nivelEnergie=Avg('nivelEnergie')).order_by('created')
        elif month == "current":
            current_month = datetime.datetime.now().month
            current_year = datetime.datetime.now().year
            data = Dream.objects.filter(user=user, created__month=current_month, created__year=current_year).annotate(
                date=TruncDate('created')).values('created').annotate(nivelEnergie=Avg('nivelEnergie')).order_by(
                'created')
        else:
            if month is not None:
                data = Dream.objects.filter(user=user, created__month=month, created__year=2023).annotate(
                    date=TruncDate('created')).values('created').annotate(nivelEnergie=Avg('nivelEnergie')).order_by(
                    'created')

        nivelEnergie_data = []
        date_labels = []
        for item in data:
            nivelEnergie_data.append(float(item['nivelEnergie']))
            date_labels.append(item['created'].strftime('%Y-%m-%d'))

        chart_data = {
            'labels': date_labels,
            'datasets': [{
                'label': 'Energy Chart',
                'data': nivelEnergie_data,
                'fill': 'false',
                'borderColor': 'rgb(0, 0, 0)',
                'lineTension': 0.1
            }]
        }
        return render(request, 'energy_chart.html', {'chart_data': chart_data})

    def create_chart_week(self, request, week):
        user = request.user.username
        data = Dream.objects.filter(user=user)
        if week is not None:
            if week != "all" and week != "current":
                data = data.filter(created__week=week)
            if week == "current":
                today = datetime.date.today()
                current_year, current_week_num, _ = today.isocalendar()
                data = data.filter(created__year=current_year, created__week=current_week_num)
        data = data.annotate(date=TruncDate('created')).values('created').annotate(
            nivelEnergie=Avg('nivelEnergie')).order_by('created')
        nivelEnergie_data = []
        date_labels = []
        for item in data:
            nivelEnergie_data.append(float(item['nivelEnergie']))
            date_labels.append(item['created'].strftime('%Y-%m-%d'))

        chart_data = {
            'labels': date_labels,
            'datasets': [{
                'label': 'Energy Chart',
                'data': nivelEnergie_data,
                'fill': 'false',
                'borderColor': 'rgb(0, 0, 0)',
                'lineTension': 0.1
            }]
        }
        return render(request, 'energy_chart.html', {'chart_data': chart_data})


class DurationChartCreator(ChartTypeCreator):
    def create_chart_month(self, request, month, year=2023):
        user = request.user.username

        if month == "all":
            data = Dream.objects.filter(user=user).annotate(date=TruncDate('created')).values('created').annotate(
                durata=Avg('durata')).order_by('created')
        elif month == "current":
            current_month = datetime.datetime.now().month
            current_year = datetime.datetime.now().year
            data = Dream.objects.filter(user=user, created__month=current_month, created__year=current_year).annotate(
                date=TruncDate('created')).values('created').annotate(durata=Avg('durata')).order_by('created')
        else:
            if month is not None:
                data = Dream.objects.filter(user=user, created__month=month, created__year=2023).annotate(
                    date=TruncDate('created')).values('created').annotate(durata=Avg('durata')).order_by('created')

        durata_data = []
        date_labels = []
        for item in data:
            durata_data.append(float(item['durata']))
            date_labels.append(item['created'].strftime('%Y-%m-%d'))

        chart_data = {
            'labels': date_labels,
            'datasets': [{
                'label': 'Duration Chart',
                'data': durata_data,
                'fill': 'false',
                'borderColor': 'rgb(0, 0, 0)',
                'lineTension': 0.1
            }]
        }
        return render(request, 'durata_chart.html', {'chart_data': chart_data})

    def create_chart_week(self, request, week):
        user = request.user.username
        data = Dream.objects.filter(user=user)
        if week is not None:
            if week != "all" and week != "current":
                data = data.filter(created__week=week)
            if week == "current":
                today = datetime.date.today()
                current_year, current_week_num, _ = today.isocalendar()
                data = data.filter(created__year=current_year, created__week=current_week_num)

        data = data.annotate(date=TruncDate('created')).values('created').annotate(durata=Avg('durata')).order_by(
            'created')
        durata_data = []
        date_labels = []
        for item in data:
            durata_data.append(float(item['durata']))
            date_labels.append(item['created'].strftime('%Y-%m-%d'))

        chart_data = {
            'labels': date_labels,
            'datasets': [{
                'label': 'Duration Chart',
                'data': durata_data,
                'fill': 'false',
                'borderColor': 'rgb(0, 0, 0)',
                'lineTension': 0.1
            }]
        }
        return render(request, 'durata_chart.html', {'chart_data': chart_data})


class ChartCreator:
    def __init__(self, chart_type):
        self.chart_type = chart_type

    def create_chart_month(self, request, month, year):
        return self.chart_type.create_chart_month(request, month, year)

    def create_chart_week(self, request, week):
        return self.chart_type.create_chart_week(request, week)
