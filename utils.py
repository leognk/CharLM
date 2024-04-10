import time
import datetime
from typing import Sequence


def get_timedelta(dt: float) -> datetime.timedelta:
    return datetime.timedelta(seconds=round(dt))


def get_timedeltas(*args: float) -> Sequence[datetime.timedelta]:
    return (get_timedelta(dt) for dt in args)


class Timer:

    def __init__(self, start=False):
        self.dt = 0
        self.start_time = None
        if start: self.start()
    
    def start(self) -> None:
        if self.start_time is None:
            self.start_time = time.time()
    
    def stop(self) -> None:
        self.dt += self.run()
        self.start_time = None
    
    def run(self) -> float:
        if self.start_time is None: return 0
        return time.time() - self.start_time
    
    def rundelta(self) -> datetime.timedelta:
        return get_timedelta(self.run())
    
    def time(self) -> float:
        return self.dt + self.run()
    
    def timedelta(self) -> datetime.timedelta:
        return get_timedelta(self.time())
    
    def state_dict(self) -> dict:
        return {"dt": self.time()}
    
    def load_state_dict(self, state_dict: dict) -> None:
        self.dt = state_dict["dt"]


class Date:

    @staticmethod
    def now() -> datetime.datetime:
        return datetime.datetime.now()
    
    @staticmethod
    def to_str(date: datetime.datetime) -> str:
        return date.strftime("%a %d %b, %H:%M:%S")
    
    @staticmethod
    def to_tuple(date: datetime.datetime) -> tuple[int]:
        return tuple(date.timetuple())[:6]


class TimeProgress:

    def __init__(self, n_iters):
        self.n_iters = n_iters
        self.timer = Timer(start=True)
        self.iter = 0
    
    def end_iter(self) -> None:
        self.iter += 1
    
    def time_progress(self) -> tuple[float, float, float]:
        dt = self.timer.time()
        total_dt = dt / self.iter * self.n_iters if self.iter != 0 else 0
        remaining_dt = total_dt - dt
        return dt, remaining_dt, total_dt
    
    @staticmethod
    def get_finish_date(remaining_dt: float) -> tuple[str, str]:
        current_time = Date.now()
        finish_time = current_time + datetime.timedelta(seconds=remaining_dt)
        current_date = Date.to_str(current_time)
        finish_date = Date.to_str(finish_time)
        return current_date, finish_date
    
    def pretty_time_progress(self) -> tuple[str, str]:
        dt, remaining_dt, total_dt = get_timedeltas(*self.time_progress())
        current_date, finish_date = TimeProgress.get_finish_date(remaining_dt)
        time_progress = f"{remaining_dt} -> {dt} / {total_dt}"
        finish_date = f"{current_date} -> {finish_date}"
        return time_progress, finish_date
    
    def pretty_iter_progress(self) -> str:
        iter_progress = f"{self.iter}/{self.n_iters} iters"
        percentage = f"{100 * self.iter / self.n_iters:.2f}%"
        return f"{iter_progress} ({percentage})"
    
    def get_str(self) -> str:
        return '\n'.join([self.pretty_time_progress(), self.pretty_iter_progress()])
    
    def state_dict(self) -> dict:
        return {
            "timer": self.timer.state_dict(),
            "iter": self.iter,
        }
    
    def load_state_dict(self, state_dict: dict) -> None:
        self.timer.load_state_dict(state_dict["timer"])
        self.iter = state_dict["iter"]