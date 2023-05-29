class Raspored:
    day_names = ['Ponedjeljak', 'Utorak', 'Srijeda', 'Četvrtak', 'Petak', 'Subota', 'Nedjelja']
    def __init__(self):
        self.weeks = {}

    def add_week_data(self, week_number, name, schedule_data):
        if week_number not in self.weeks:
            self.weeks[week_number] = {}
        if name not in self.weeks[week_number]:
            self.weeks[week_number][name] = []
        day_schedule = {day: schedule for day, schedule in zip(self.day_names, schedule_data)}
        self.weeks[week_number][name].append(day_schedule)

    def get_last_schedule_version(self, week_number, name):
        if week_number in self.weeks and name in self.weeks[week_number]:
            schedules = self.weeks[week_number][name]
            if schedules:
                return schedules[-1]
        return None

    def get_all_last_versions(self):
        last_versions = {}
        for week_number, week_data in self.weeks.items():
            for name, schedules in week_data.items():
                if schedules:
                    last_versions[name] = schedules[-1]
        return last_versions

    def get_week_data(self, week_number):
        return self.weeks.get(week_number, {})

    def get_versions_count(self, week_number, name):
        if week_number in self.weeks and name in self.weeks[week_number]:
            return len(self.weeks[week_number][name])
        return 0

    def get_weeks(self):
        return self.weeks