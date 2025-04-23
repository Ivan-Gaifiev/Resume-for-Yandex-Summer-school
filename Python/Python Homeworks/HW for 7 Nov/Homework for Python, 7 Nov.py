import Interaction as Inter


def main():
    num_timers = Inter.inp_num_timers()
    dict_time = Inter.inp_time_work(num_timers)
    Inter.timer_launch(dict_time)


if __name__ == "__main__":
    main()
