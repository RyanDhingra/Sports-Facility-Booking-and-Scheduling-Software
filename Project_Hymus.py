from tkinter import *
from tkinter import ttk
from tkinter.tix import NoteBook
from PIL import ImageTk, Image
import datetime

activated_list = []
startup_list = []

def prebooking(): #Pre-booking allows you to create daily, weekly, or bi-weekly bookings for an entire month with 1 step.
    
    '''Window Settingss'''
    prebooking_window = Toplevel()
    prebooking_window.title("Booking Information")
    prebooking_window.geometry("400x1100")
    prebooking_window.configure(bg='lightblue')

    '''Logo Image'''
    img = Image.open('hymussportslogo.png')
    resized_img = img.resize((400, 200), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(resized_img)
    logo_label = Label(prebooking_window, image=logo).pack()

    '''User Inputs'''
    time_choice_list = ['12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM', '12AM']
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    days = [x for x in range(1, 32)]
    days_by_month = [31,29,31,30,31,30,31,31,30,31,30,31]
    courts = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    hours = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    prebooking_options = ["Weekly","Daily","Bi-Weekly"]

    booking_name = Label(prebooking_window, text = "Enter Customer Name:", fg="black", bg="lightblue", font=(16)).place(x=14, y=210)
    entry1 = Entry(prebooking_window, width=41, font=(16))
    entry1.place(x=14,y=240)

    phone_num = Label(prebooking_window, text = "Enter Phone Number:", fg="black", bg="lightblue", font=(16)).place(x=14, y=310)
    entry2 = Entry(prebooking_window, width=41, font=(16))
    entry2.place(x=14,y=340)

    starttime = StringVar()
    starttime.set(time_choice_list[0])
    start_time = Label(prebooking_window, text = "Enter Start Time:", fg="black", bg="lightblue", font=(16)).place(x=15, y=410)
    start_time_menu = OptionMenu(prebooking_window, starttime, *time_choice_list)
    start_time_menu.config(width=37, font=(16))
    start_time_menu.config(highlightthickness=0)
    start_time_menu.place(x=14,y=440)
    
    hour_num = StringVar()
    hour_num.set(hours[0])
    hour_label = Label(prebooking_window, text = "Enter Booking Length:", fg="black", bg="lightblue", font=(16)).place(x=15, y=510)
    hour_num_menu = OptionMenu(prebooking_window, hour_num, *hours)
    hour_num_menu.config(width=37, font=(16))
    hour_num_menu.config(highlightthickness=0)
    hour_num_menu.place(x=14,y=540)

    booking_month = StringVar()
    booking_month.set(months[0])
    month_label = Label(prebooking_window, text = "Select Month:", fg="black", bg="lightblue", font=(16)).place(x=15, y=610)
    month_menu = OptionMenu(prebooking_window, booking_month, *months)
    month_menu.config(width=37, font=(16))
    month_menu.config(highlightthickness=0)
    month_menu.place(x=14,y=640)

    booking_day = StringVar()
    booking_day.set(days[0])
    day_num = Label(prebooking_window, text = "Select Start Date:", fg="black", bg="lightblue", font=(16)).place(x=15, y=710)
    day_menu = OptionMenu(prebooking_window, booking_day, *days)
    day_menu.config(width=37, font=(16))
    day_menu.config(highlightthickness=0)
    day_menu.place(x=14,y=740)

    prebooking_frequency = StringVar()
    prebooking_frequency.set(prebooking_options[0])
    prebooking_label = Label(prebooking_window, text = "Select Booking Frequency:", fg="black", bg="lightblue", font=(16)).place(x=15, y=810)
    prebooking_menu = OptionMenu(prebooking_window, prebooking_frequency, *prebooking_options)
    prebooking_menu.config(width=37, font=(16))
    prebooking_menu.config(highlightthickness=0)
    prebooking_menu.place(x=14,y=840)

    court = Label(prebooking_window, text = "Enter court numbers separated by commas:", fg="black", bg="lightblue", font=(16)).place(x=15, y=910)
    court_nums = Entry(prebooking_window, width=41, font=(16))
    court_nums.place(x=14,y=940)

    def get_booking_info(): #Pre-booking helper function.

        '''Error Handlers''' 
        if (entry1.get() == ''):
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'Please enter customer name.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            error_window.mainloop()
        elif entry2.get().isdigit() == False:
            error_window = Toplevel()
            error_window.geometry("275x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'Please enter a valid customer number.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            error_window.mainloop()
        elif ((booking_month.get() == "April") or (booking_month.get() == "June") or (booking_month.get() == "September") or (booking_month.get() == "November")) and (int(booking_day.get()) == 31):
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'Please enter a valid date.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            error_window.mainloop()
        elif (booking_month.get() == "February") and (int(booking_day.get()) >= 30):
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'Please enter a valid date.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            error_window.mainloop()
        elif court_nums.get() == '':
            error_window = Toplevel()
            error_window.geometry("360x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'Please enter court numbers separated by commas.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            error_window.mainloop()
        else:
            list_of_times = []
            current_slot = []
            list_of_time_slots = []
            first_hour = time_choice_list.index(starttime.get())
            court_num_list = court_nums.get().split(',')
            duplicate_checker = []
            
            for x in court_num_list:
                if x not in duplicate_checker:
                    duplicate_checker.append(x)
                else:
                    x in duplicate_checker
                    error_window = Toplevel()
                    error_window.geometry("260x85")
                    error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
                    help_message = Label(error_window, text = 'Please enter court numbers once.', fg="black", font=16).pack()
                    exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
                    error_window.mainloop()

            if prebooking_frequency.get() == "Daily":
                day_list = days[days.index(int(booking_day.get())):days_by_month[months.index(booking_month.get())]]
            elif prebooking_frequency.get() == "Weekly":
                day_list = days[days.index(int(booking_day.get())):days_by_month[months.index(booking_month.get())]:7]
            elif prebooking_frequency.get() == "Bi-Weekly":
                day_list = days[days.index(int(booking_day.get())):days_by_month[months.index(booking_month.get())]:14]

            for x in court_num_list:
                if (x not in courts) or (x.isdigit() == False):
                    error_window = Toplevel()
                    error_window.geometry("260x85")
                    error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
                    help_message = Label(error_window, text = 'Please enter valid court numbers.', fg="black", font=16).pack()
                    exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
                    error_window.mainloop()

            while int(hour_num.get()) <= 24:
                if (first_hour + int(hour_num.get())) < len(time_choice_list):
                    for x in range(first_hour, first_hour + int(hour_num.get()) + 1):
                        list_of_times.append(time_choice_list[x])
                    break
                else:
                    error_window = Toplevel()
                    error_window.geometry("260x85")
                    error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
                    help_message = Label(error_window, text = 'Daily timeslots exceeded.', fg="black", font=16).pack()
                    exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
                    error_window.mainloop()
                    
            x = 0

            while x < len(list_of_times) - 1:
                current_slot.append(list_of_times[x])
                current_slot.append(list_of_times[x + 1])
                x += 1
                list_of_time_slots.append(current_slot)
                current_slot = []
            
            '''File Writer'''
            time_slots = [['12AM', '1AM'], ['1AM', '2AM'], ['2AM', '3AM'], ['3AM', '4AM'], ['4AM', '5AM'], ['5AM', '6AM'], ['6AM', '7AM'], ['7AM', '8AM'], ['8AM', '9AM'], ['9AM', '10AM'], ['10AM', '11AM'], ['11AM', '12PM'], ['12PM', '1PM'], ['1PM', '2PM'], ['2PM', '3PM'], ['3PM', '4PM'], ['4PM', '5PM'], ['5PM', '6PM'], ['6PM', '7PM'], ['7PM', '8PM'], ['8PM', '9PM'], ['9PM', '10PM'], ['10PM', '11PM'], ['11PM', '12AM']]

            input_name = entry1.get()
            input_num = entry2.get()
            input_month = booking_month.get()
            time_range = [list_of_time_slots[0][0], list_of_time_slots[-1][-1]]
            length_num = hour_num.get()

            court_functions = [january_courts, february_courts, march_courts, april_courts, may_courts, june_courts, july_courts, august_courts, september_courts, october_courts, november_courts, december_courts]
            
            if input_month not in activated_list:
                court_functions[months.index(input_month)]()
                activated_list.append(input_month)

            for day in day_list:
                for times in list_of_time_slots:
                    for court in court_num_list:
                        input_courtnum = int(court)
                        input_day = int(day)
                        booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)

            prebooking_window.destroy()
        
    '''Command Buttons'''
    finish = Button(prebooking_window, text="Complete Booking", command=get_booking_info, fg="white", bg="#008B00", font=16).place(x=127,y=995)
    cancel = Button(prebooking_window, text="Cancel", command=prebooking_window.destroy, fg="white", bg="red", font=16).place(x=169,y=1055)

    prebooking_window.mainloop() 

def customer_display(): #Live customer display that updates automatically every hour.
    
    current_time = datetime.datetime.now()
    month = current_time.strftime('%m')
    list_of_months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if list_of_months[int(month) - 1] in activated_list:

        root = Toplevel() 
        root.title("Court Display")
        screen_width = str(root.winfo_screenwidth())
        screen_height = str(root.winfo_screenheight())
        root.geometry(screen_width + 'x' + screen_height + '+0+0')
        root.configure(bg = 'lightblue')
        court_img = Image.open("court.png")
        resized_court = court_img.resize((152, 197), Image.ANTIALIAS)
        court_bg = ImageTk.PhotoImage(resized_court)

        a = 0
        while a < 10:
            columnplaceholder = Label(root, text="                                                               ", bg= "lightblue").grid(row = 0, column=a)
            a += 2
        
        for x in range(3,13,3):
            row_placeholder = Label(root, text=" ", bg= "lightblue").grid(row = x, column=1)

        court_num = 1
        for a in range(1,10,2):
            for b in range(1,11,3):
                court_number = Label(root, text=f"Court {court_num}", bg= "lightblue", font=16).grid(row=b, column=a)
                court_num +=1

        displaycourt_list = []

        for a in range(1,10,2):
            for b in range(2,12,3):
                display_court = Text(root, width=17, height=11, font=16, bg = "#008B00")
                display_court.image_create(END, image=court_bg)
                display_court.grid(row=b, column=a)
                displaycourt_list.append(display_court)

        def updater(): #Customer diplay helper funtion.

            current_time = datetime.datetime.now()
            month = current_time.strftime('%m')
            mins = current_time.strftime('%M')
            day = current_time.strftime('%d')
            hour = current_time.strftime('%H')
            secs = current_time.strftime('%S')
            time_delay = ((60 - int(mins)) * 60) - int(secs)
            month_courtlists = [jan_courtlist, feb_courtlist, mar_courtlist, apr_courtlist, may_courtlist, jun_courtlist, jul_courtlist, aug_courtlist, sep_courtlist, oct_courtlist, nov_courtlist, dec_courtlist]

            while list_of_months[int(month) - 1] in activated_list:

                for mth in list_of_months:
                    if mth == list_of_months[int(month) - 1]:
                        courtlist = month_courtlists[list_of_months.index(mth)]
                        courts = []

                        for x in range(20):
                            court = courtlist[((((int(day)-1)*24) + int(hour)) * 20) + x].get(1.0, END).split('\n')
                            courts.append(court)
                        
                        for court in courts:
                            if court != ['','']:
                                displaycourt_list[courts.index(court)].delete(1.0, END)
                                displaycourt_list[courts.index(court)].insert(END, court[0] + '\n')
                                displaycourt_list[courts.index(court)].insert(END, court[2])
                                displaycourt_list[courts.index(court)].config(bg='#00688B', fg="white")
                            else:
                                displaycourt_list[courts.index(court)].delete(1.0, END)
                                displaycourt_list[courts.index(court)].config(bg="#008B00")
                                displaycourt_list[courts.index(court)].image_create(END, image=court_bg)
                break
            root.after((time_delay * 1000), updater)  
        updater()
        root.mainloop()

    else:
        error_window = Toplevel()
        error_window.geometry("350x85")
        error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
        help_message = Label(error_window, text = 'Please load bookings before displaying.', fg="black", font=16).pack()
        exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
        error_window.mainloop()
    
    

def start_up(): #The start-up function automatically re-inserts all booking.

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    court_functions = [january_courts, february_courts, march_courts, april_courts, may_courts, june_courts, july_courts, august_courts, september_courts, october_courts, november_courts, december_courts]

    '''Window Settings'''
    startup_window = Toplevel()
    startup_window.title("Court Loading")
    startup_window.geometry("400x400")
    startup_window.configure(bg='lightblue')

    '''Logo Image'''
    img = Image.open('hymussportslogo.png')
    resized_img = img.resize((400, 200), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(resized_img)
    logo_label = Label(startup_window, image=logo).pack()

    '''Inputs'''
    booking_month = StringVar()
    booking_month.set(months[0])
    month_label = Label(startup_window, text = "Select Month:", fg="black", bg="lightblue", font=(16)).place(x=15, y=210)
    month_menu = OptionMenu(startup_window, booking_month, *months)
    month_menu.config(width=37, font=(16))
    month_menu.config(highlightthickness=0)
    month_menu.place(x=14,y=240)

    def insertion_function(): #Start-up helper function.

        time_choice_list = ['12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM', '12AM']
        month = booking_month.get()
        line_list = []

        with open("bookingDataStorage.txt", 'r') as f:    
            for line in f:
                line_list.append(line.strip('\n'))

        f.close()

        months_not_added = []

        for x in range(4, len(line_list), 6):
            if month not in line_list[x]:
                if month not in months_not_added:
                    months_not_added.append(month)
            elif month in line_list[x]:
                if month in months_not_added:
                    months_not_added.remove(month)
                break
                    
        if len(months_not_added) != 0:
            error_window = Toplevel()
            error_window.geometry("300x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'There are no bookings to load.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            error_window.mainloop()

        if line_list == []:
            error_window = Toplevel()
            error_window.geometry("300x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'There are no bookings to load.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            error_window.mainloop()
        else:
            line_list != []
            
            if month not in startup_list:
                x = 0

                while x < len(line_list) - 1:
                
                    name = line_list[x]
                    num = line_list[x + 1]
                    startingtime = line_list[x + 2]
                    length = int(line_list[x + 3])
                    date = line_list[x + 4]
                    code = line_list[x + 5]

                    for y in time_choice_list:
                        if y == startingtime.strip('\n'):
                            starting_index = time_choice_list.index(y)
                    
                    ending_index = starting_index + length
                    time_info = [time_choice_list[starting_index], time_choice_list[ending_index]]

                    for mth in months:
                        if month == mth and mth in date:
                            if month not in activated_list:
                                court_functions[months.index(mth)]()
                                startup_insertion(name, num, code, month, time_info)
                                activated_list.append(mth)
                            else:
                                startup_insertion(name, num, code, month, time_info)
                    x += 6

                startup_window.destroy() 
            else:
                error_window = Toplevel()
                error_window.geometry("330x85")
                error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
                help_message = Label(error_window, text = 'Bookings have already been loaded.', fg="black", font=16).pack()
                exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
                error_window.mainloop()

            startup_list.append(month)  
    
    '''Command Buttons'''
    load_courts = Button(startup_window, text="Load Courts", command=insertion_function, fg="white", bg="#008B00", font=16).place(x=149,y=285)
    cancel = Button(startup_window, text="Cancel", command=startup_window.destroy, fg="white", bg="red", font=16).place(x=169,y=350)

    startup_window.mainloop()
        
def booking_info(): #Creates bookings for given user inputs.

    '''Window Settingss'''
    info_window = Toplevel()
    info_window.title("Booking Information")
    info_window.geometry("400x1000")
    info_window.configure(bg='lightblue')

    '''Logo Image'''
    img = Image.open('hymussportslogo.png')
    resized_img = img.resize((400, 200), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(resized_img)
    logo_label = Label(info_window, image=logo).pack()

    '''User Inputs'''
    time_choice_list = ['12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM', '12AM']
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    courts = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
    hours = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

    booking_name = Label(info_window, text = "Enter Customer Name:", fg="black", bg="lightblue", font=(16)).place(x=14, y=210)
    entry1 = Entry(info_window, width=41, font=(16))
    entry1.place(x=14,y=240)

    phone_num = Label(info_window, text = "Enter Phone Number:", fg="black", bg="lightblue", font=(16)).place(x=14, y=310)
    entry2 = Entry(info_window, width=41, font=(16))
    entry2.place(x=14,y=340)

    starttime = StringVar()
    starttime.set(time_choice_list[0])
    start_time = Label(info_window, text = "Enter Start Time:", fg="black", bg="lightblue", font=(16)).place(x=15, y=410)
    start_time_menu = OptionMenu(info_window, starttime, *time_choice_list)
    start_time_menu.config(width=37, font=(16))
    start_time_menu.config(highlightthickness=0)
    start_time_menu.place(x=14,y=440)
    
    hour_num = StringVar()
    hour_num.set(hours[0])
    hour_label = Label(info_window, text = "Enter Booking Length:", fg="black", bg="lightblue", font=(16)).place(x=15, y=510)
    hour_num_menu = OptionMenu(info_window, hour_num, *hours)
    hour_num_menu.config(width=37, font=(16))
    hour_num_menu.config(highlightthickness=0)
    hour_num_menu.place(x=14,y=540)

    booking_month = StringVar()
    booking_month.set(months[0])
    month_label = Label(info_window, text = "Select Month:", fg="black", bg="lightblue", font=(16)).place(x=15, y=610)
    month_menu = OptionMenu(info_window, booking_month, *months)
    month_menu.config(width=37, font=(16))
    month_menu.config(highlightthickness=0)
    month_menu.place(x=14,y=640)

    booking_day = StringVar()
    booking_day.set(days[0])
    day_num = Label(info_window, text = "Select Date:", fg="black", bg="lightblue", font=(16)).place(x=15, y=710)
    day_menu = OptionMenu(info_window, booking_day, *days)
    day_menu.config(width=37, font=(16))
    day_menu.config(highlightthickness=0)
    day_menu.place(x=14,y=740)

    court = Label(info_window, text = "Enter court numbers separated by commas:", fg="black", bg="lightblue", font=(16)).place(x=15, y=810)
    court_nums = Entry(info_window, width=41, font=(16))
    court_nums.place(x=14,y=840) 

    '''Information Getter'''
    def get_booking_info(): #Booking creation funcion.

        if (entry1.get() == ''):
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'Please enter customer name.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            error_window.mainloop()
        elif entry2.get().isdigit() == False:
            error_window = Toplevel()
            error_window.geometry("275x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'Please enter a valid customer number.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            error_window.mainloop()
        elif ((booking_month.get() == "April") or (booking_month.get() == "June") or (booking_month.get() == "September") or (booking_month.get() == "November")) and (int(booking_day.get()) == 31):
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'Please enter a valid date.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            error_window.mainloop()
        elif (booking_month.get() == "February") and (int(booking_day.get()) >= 30):
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'Please enter a valid date.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            error_window.mainloop()
        elif court_nums.get() == '':
            error_window = Toplevel()
            error_window.geometry("360x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'Please enter court numbers separated by commas.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            error_window.mainloop()
        else:
            list_of_times = []
            current_slot = []
            list_of_time_slots = []
            court_num_list = court_nums.get().split(',')
            first_hour = time_choice_list.index(starttime.get())
            duplicate_checker = []
            court_functions = [january_courts, february_courts, march_courts, april_courts, may_courts, june_courts, july_courts, august_courts, september_courts, october_courts, november_courts, december_courts]
            
            for x in court_num_list:
                if x not in duplicate_checker:
                    duplicate_checker.append(x)
                else:
                    x in duplicate_checker
                    error_window = Toplevel()
                    error_window.geometry("260x85")
                    error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
                    help_message = Label(error_window, text = 'Please enter court numbers once.', fg="black", font=16).pack()
                    exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
                    error_window.mainloop()

            for x in court_num_list:
                if (x not in courts) or (x.isdigit() == False):
                    error_window = Toplevel()
                    error_window.geometry("260x85")
                    error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
                    help_message = Label(error_window, text = 'Please enter valid court numbers.', fg="black", font=16).pack()
                    exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
                    error_window.mainloop()

            while int(hour_num.get()) <= 24:
                if (first_hour + int(hour_num.get())) < len(time_choice_list):
                    for x in range(first_hour, first_hour + int(hour_num.get()) + 1):
                        list_of_times.append(time_choice_list[x])
                    break
                else:
                    error_window = Toplevel()
                    error_window.geometry("260x85")
                    error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
                    help_message = Label(error_window, text = 'Daily timeslots exceeded.', fg="black", font=16).pack()
                    exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
                    error_window.mainloop()
                    
            x = 0

            while x < len(list_of_times) - 1:
                current_slot.append(list_of_times[x])
                current_slot.append(list_of_times[x + 1])
                x += 1
                list_of_time_slots.append(current_slot)
                current_slot = []

            input_name = entry1.get()
            input_num = entry2.get()
            input_month = booking_month.get()
            input_day = int(booking_day.get())
            time_range = [list_of_time_slots[0][0], list_of_time_slots[-1][-1]]
            length_num = hour_num.get()
            
            '''Court Activator'''
            for mth in months:
                if mth == input_month:
                    if input_month not in activated_list:
                        court_functions[months.index(mth)]()
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                        activated_list.append(mth)
                    else:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)

            info_window.destroy()
        
    '''Command Buttons'''
    finish = Button(info_window, text="Complete Booking", command=get_booking_info, fg="white", bg="#008B00", font=16).place(x=127,y=895)
    cancel = Button(info_window, text="Cancel", command=info_window.destroy, fg="white", bg="red", font=16).place(x=169,y=955)

    info_window.mainloop()

def cancellation_info(): #Cancels bookings using booking IDs.
    
    '''Window Settingss'''
    cancellation_window = Toplevel()
    cancellation_window.title("Court Cancellation")
    cancellation_window.geometry("400x500")
    cancellation_window.configure(bg='lightblue')

    '''Logo Image'''
    img = Image.open('hymussportslogo.png')
    resized_img = img.resize((400, 200), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(resized_img)
    logo_label = Label(cancellation_window, image=logo).pack()

    '''User Inputs'''
    time_slots = [['12AM', '1AM'], ['1AM', '2AM'], ['2AM', '3AM'], ['3AM', '4AM'], ['4AM', '5AM'], ['5AM', '6AM'], ['6AM', '7AM'], ['7AM', '8AM'], ['8AM', '9AM'], ['9AM', '10AM'], ['10AM', '11AM'], ['11AM', '12PM'], ['12PM', '1PM'], ['1PM', '2PM'], ['2PM', '3PM'], ['3PM', '4PM'], ['4PM', '5PM'], ['5PM', '6PM'], ['6PM', '7PM'], ['7PM', '8PM'], ['8PM', '9PM'], ['9PM', '10PM'], ['10PM', '11PM'], ['11PM', '12AM']]
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    for x in time_slots:
        if x == time_slots:
            timeslot_index = time_slots.index(x)

    booking_month = StringVar()
    booking_month.set(months[0])
    month_label = Label(cancellation_window, text = "Select Month:", fg="black", bg="lightblue", font=(16)).place(x=15, y=210)
    month_menu = OptionMenu(cancellation_window, booking_month, *months)
    month_menu.config(width=37, font=(16))
    month_menu.config(highlightthickness=0)
    month_menu.place(x=14,y=240)

    booking_id = Label(cancellation_window, text = "Enter Booking ID(s):", fg="black", bg="lightblue", font=(16)).place(x=14, y=310)
    id = Entry(cancellation_window, width=41, font=(16))
    id.place(x=14,y=340)

    '''Information Getter'''
    def booking_deletion(): #Booking cancellation helper function.
        
        id_list = id.get().split(',')
        
        for x in id_list:
            if x.isdigit() == False:
                error_window = Toplevel()
                error_window.geometry("260x85")
                error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
                help_message = Label(error_window, text = 'Please enter valid ID(s).', fg="black", font=16).pack()
                exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
                error_window.mainloop()

        if id_list == []:
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'Please enter valid ID(s).', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            error_window.mainloop()
        elif booking_month.get() not in activated_list:
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'Please load courts before cancelling.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            error_window.mainloop()
        else:
            list_of_lines = []

            with open("bookingDataStorage.txt", "r") as f:
                        for line in f:
                            clean_line = line.strip('\n')
                            list_of_lines.append(clean_line.strip('Location Code: '))
            f.close()
            
            for z in id_list:
                if z in list_of_lines:
                    line_list = []
                    clean_linelist = []
                    
                    with open("bookingDataStorage.txt", "r") as f:
                        for line in f:
                            line_list.append(line.strip("\n"))
                    f.close()
                    
                    for x in range(0, len(line_list)):
                        if (z == line_list[x].strip('Location Code: ')) and (booking_month.get() in line_list[x-1]):
                            code_line = line_list[x]
                            a = line_list.index(code_line)
                            b = a-5
                            counter = 0

                            for x in line_list:
                                if (counter < b) or (counter > a):
                                    clean_linelist.append(x)
                                counter += 1
                    
                    with open("bookingDataStorage.txt", "w") as f:
                            for x in clean_linelist:
                                if (x != '') and (x != "\n"):
                                    f.write(x)
                                    f.write("\n")
                    f.close()
                    input_month = booking_month.get()
                       
                    booking_canceller(input_month, int(z))
                    cancellation_window.destroy()
                else:
                    error_window = Toplevel()
                    error_window.geometry("330x85")
                    error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
                    help_message = Label(error_window, text = 'Invalid booking entered.', fg="black", font=16).pack()
                    exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
                    error_window.mainloop()

    finish = Button(cancellation_window, text="Complete Cancellation", command=booking_deletion, fg="white", bg="#008B00", font=16).place(x=117,y=375)
    cancel = Button(cancellation_window, text="Cancel", command=cancellation_window.destroy, fg="white", bg="red", font=16).place(x=169,y=450)

    cancellation_window.mainloop()

schedule_window = Tk()
schedule_window.title("Badminton Scheduling Software")
schedule_window.configure(bg='lightblue')
screen_width = str(schedule_window.winfo_screenwidth())
screen_height = str(schedule_window.winfo_screenheight())
schedule_window.geometry(screen_width + 'x' + screen_height + '+0+0')
new_booking = Button(schedule_window, text="Create New Booking", command=booking_info, fg="white", bg="#00688B", font=16).place(x=638, y=0)
cancellation = Button(schedule_window, text="Cancellation", command=cancellation_info, fg="white", bg="#00688B", font=16).place(x=797, y=0)
startup_button = Button(schedule_window, text="Load Bookings", command=start_up, fg="white", bg="#00688B", font=16).place(x=897, y=0)
display_button = Button(schedule_window, text="Open Display", command=customer_display, fg="white", bg="#00688B", font=16).place(x=1017, y=0)
prebooking_button = Button(schedule_window, text="Create Pre-Booking", command=prebooking, fg="white", bg="#00688B", font=16).place(x=1125, y=0)

'''Tab Loop'''
year = ttk.Notebook(schedule_window)
year.pack(pady=32, fill="both")

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
days = [31,29,31,30,31,30,31,31,30,31,30,31]
time_slots = [['12AM - 1AM'], ['1AM - 2AM'], ['2AM - 3AM'], ['3AM - 4AM'], ['4AM - 5AM'], ['5AM - 6AM'], ['6AM - 7AM'], ['7AM - 8AM'], ['8AM - 9AM'], ['9AM - 10AM'], ['10AM - 11AM'], ['11AM - 12PM'], ['12PM - 1PM'], ['1PM - 2PM'], ['2PM - 3PM'], ['3PM - 4PM'], ['4PM - 5PM'], ['5PM - 6PM'], ['6PM - 7PM'], ['7PM - 8PM'], ['8PM - 9PM'], ['9PM - 10PM'], ['10PM - 11PM'], ['11PM - 12AM']]
court_times = []

for x in range(0,12):
    month_frame = Frame(year, width=screen_width, height=screen_height, bg= "lightblue")
    month_frame.pack(fill="both", expand=1)
    year.add(month_frame, text=months[x])
    date_tabs = ttk.Notebook(month_frame)
    date_tabs.pack(fill="both")
    for y in range(1, days[x] + 1):
        date = Frame(date_tabs, width=screen_width, height=screen_height, bg= "lightblue")
        date.pack(fill="both")
        date_tabs.add(date, text=y)
        time_tabs = ttk.Notebook(date)
        time_tabs.pack(fill="both")
        for z in range(0,24):
            times = Frame(time_tabs, width=screen_width, height=screen_height, bg= "lightblue")
            times.pack(fill="both")
            time_tabs.add(times, text=time_slots[z][0])
            court_times.append(times)

jan_courtlist = []
feb_courtlist = []
mar_courtlist = []
apr_courtlist = []
may_courtlist = []
jun_courtlist = []
jul_courtlist = []
aug_courtlist = []
sep_courtlist = []
oct_courtlist = []
nov_courtlist = []
dec_courtlist = []

'''Court Creating Functions'''

def january_courts():
    for x in court_times[0:744]:
        for a in range(0,9,2):
            column_placeholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=a)

        for a in range(3,13,3):
            row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = a, column=1)

        court_num = 1
        for a in range(1,10,2):
            for b in range(1,11,3):
                court_number = Label(x, text=f"Court {court_num}", bg= "lightblue", font=16).grid(row=b, column=a)
                court_num += 1
        
        for a in range(1,10,2):
            for b in range(2,12,3):
                court_text = Text(x, width=15, height=10, font=16, bg = "#008B00")
                court_text.grid(row=b, column=a)
                jan_courtlist.append(court_text)

def february_courts():
    for x in court_times[744:1440]:
        for a in range(0,9,2):
            column_placeholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=a)

        for a in range(3,13,3):
            row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = a, column=1)

        court_num = 1
        for a in range(1,10,2):
            for b in range(1,11,3):
                court_number = Label(x, text=f"Court {court_num}", bg= "lightblue", font=16).grid(row=b, column=a)
                court_num += 1
        
        for a in range(1,10,2):
            for b in range(2,12,3):
                court_text = Text(x, width=15, height=10, font=16, bg = "#008B00")
                court_text.grid(row=b, column=a)
                feb_courtlist.append(court_text)

def march_courts():
    for x in court_times[1440:2184]:
        for a in range(0,9,2):
            column_placeholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=a)

        for a in range(3,13,3):
            row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = a, column=1)

        court_num = 1
        for a in range(1,10,2):
            for b in range(1,11,3):
                court_number = Label(x, text=f"Court {court_num}", bg= "lightblue", font=16).grid(row=b, column=a)
                court_num += 1
        
        for a in range(1,10,2):
            for b in range(2,12,3):
                court_text = Text(x, width=15, height=10, font=16, bg = "#008B00")
                court_text.grid(row=b, column=a)
                mar_courtlist.append(court_text)

def april_courts():
    for x in court_times[2184:2904]:
        for a in range(0,9,2):
            column_placeholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=a)

        for a in range(3,13,3):
            row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = a, column=1)

        court_num = 1
        for a in range(1,10,2):
            for b in range(1,11,3):
                court_number = Label(x, text=f"Court {court_num}", bg= "lightblue", font=16).grid(row=b, column=a)
                court_num += 1
        
        for a in range(1,10,2):
            for b in range(2,12,3):
                court_text = Text(x, width=15, height=10, font=16, bg = "#008B00")
                court_text.grid(row=b, column=a)
                apr_courtlist.append(court_text)


def may_courts():
    for x in court_times[2904:3648]:
        for a in range(0,9,2):
            column_placeholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=a)

        for a in range(3,13,3):
            row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = a, column=1)

        court_num = 1
        for a in range(1,10,2):
            for b in range(1,11,3):
                court_number = Label(x, text=f"Court {court_num}", bg= "lightblue", font=16).grid(row=b, column=a)
                court_num += 1
        
        for a in range(1,10,2):
            for b in range(2,12,3):
                court_text = Text(x, width=15, height=10, font=16, bg = "#008B00")
                court_text.grid(row=b, column=a)
                may_courtlist.append(court_text)


def june_courts():
    for x in court_times[3648:4368]:
        for a in range(0,9,2):
            column_placeholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=a)

        for a in range(3,13,3):
            row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = a, column=1)

        court_num = 1
        for a in range(1,10,2):
            for b in range(1,11,3):
                court_number = Label(x, text=f"Court {court_num}", bg= "lightblue", font=16).grid(row=b, column=a)
                court_num += 1
        
        for a in range(1,10,2):
            for b in range(2,12,3):
                court_text = Text(x, width=15, height=10, font=16, bg = "#008B00")
                court_text.grid(row=b, column=a)
                jun_courtlist.append(court_text)

def july_courts():
    for x in court_times[4368:5112]:
        for a in range(0,9,2):
            column_placeholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=a)

        for a in range(3,13,3):
            row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = a, column=1)

        court_num = 1
        for a in range(1,10,2):
            for b in range(1,11,3):
                court_number = Label(x, text=f"Court {court_num}", bg= "lightblue", font=16).grid(row=b, column=a)
                court_num += 1
        
        for a in range(1,10,2):
            for b in range(2,12,3):
                court_text = Text(x, width=15, height=10, font=16, bg = "#008B00")
                court_text.grid(row=b, column=a)
                jul_courtlist.append(court_text)

def august_courts():
    for x in court_times[5112:5856]:
        for a in range(0,9,2):
            column_placeholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=a)

        for a in range(3,13,3):
            row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = a, column=1)

        court_num = 1
        for a in range(1,10,2):
            for b in range(1,11,3):
                court_number = Label(x, text=f"Court {court_num}", bg= "lightblue", font=16).grid(row=b, column=a)
                court_num += 1
        
        for a in range(1,10,2):
            for b in range(2,12,3):
                court_text = Text(x, width=15, height=10, font=16, bg = "#008B00")
                court_text.grid(row=b, column=a)
                aug_courtlist.append(court_text)

def september_courts():
    for x in court_times[5856:6576]:
        for a in range(0,9,2):
            column_placeholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=a)

        for a in range(3,13,3):
            row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = a, column=1)

        court_num = 1
        for a in range(1,10,2):
            for b in range(1,11,3):
                court_number = Label(x, text=f"Court {court_num}", bg= "lightblue", font=16).grid(row=b, column=a)
                court_num += 1
        
        for a in range(1,10,2):
            for b in range(2,12,3):
                court_text = Text(x, width=15, height=10, font=16, bg = "#008B00")
                court_text.grid(row=b, column=a)
                sep_courtlist.append(court_text)

def october_courts():
    for x in court_times[6576:7320]:
        for a in range(0,9,2):
            column_placeholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=a)

        for a in range(3,13,3):
            row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = a, column=1)

        court_num = 1
        for a in range(1,10,2):
            for b in range(1,11,3):
                court_number = Label(x, text=f"Court {court_num}", bg= "lightblue", font=16).grid(row=b, column=a)
                court_num += 1
        
        for a in range(1,10,2):
            for b in range(2,12,3):
                court_text = Text(x, width=15, height=10, font=16, bg = "#008B00")
                court_text.grid(row=b, column=a)
                oct_courtlist.append(court_text)

def november_courts():
    for x in court_times[7320:8040]:
        for a in range(0,9,2):
            column_placeholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=a)

        for a in range(3,13,3):
            row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = a, column=1)

        court_num = 1
        for a in range(1,10,2):
            for b in range(1,11,3):
                court_number = Label(x, text=f"Court {court_num}", bg= "lightblue", font=16).grid(row=b, column=a)
                court_num += 1
        
        for a in range(1,10,2):
            for b in range(2,12,3):
                court_text = Text(x, width=15, height=10, font=16, bg = "#008B00")
                court_text.grid(row=b, column=a)
                nov_courtlist.append(court_text)

def december_courts():
    for x in court_times[8040:8784]:
        for a in range(0,9,2):
            column_placeholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=a)

        for a in range(3,13,3):
            row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = a, column=1)

        court_num = 1
        for a in range(1,10,2):
            for b in range(1,11,3):
                court_number = Label(x, text=f"Court {court_num}", bg= "lightblue", font=16).grid(row=b, column=a)
                court_num += 1
        
        for a in range(1,10,2):
            for b in range(2,12,3):
                court_text = Text(x, width=15, height=10, font=16, bg = "#008B00")
                court_text.grid(row=b, column=a)
                dec_courtlist.append(court_text)

'''Booking Creator'''
def booking_insertion(name, number, month, day, timeslot, court_num, time_stamp, length_input): #Enters booking information into the employee display.
    
    time_slots = [['12AM', '1AM'], ['1AM', '2AM'], ['2AM', '3AM'], ['3AM', '4AM'], ['4AM', '5AM'], ['5AM', '6AM'], ['6AM', '7AM'], ['7AM', '8AM'], ['8AM', '9AM'], ['9AM', '10AM'], ['10AM', '11AM'], ['11AM', '12PM'], ['12PM', '1PM'], ['1PM', '2PM'], ['2PM', '3PM'], ['3PM', '4PM'], ['4PM', '5PM'], ['5PM', '6PM'], ['6PM', '7PM'], ['7PM', '8PM'], ['8PM', '9PM'], ['9PM', '10PM'], ['10PM', '11PM'], ['11PM', '12AM']]
    
    for x in time_slots:
        if x == timeslot:
            timeslot_index = time_slots.index(x)
    
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_courtlists = [jan_courtlist, feb_courtlist, mar_courtlist, apr_courtlist, may_courtlist, jun_courtlist, jul_courtlist, aug_courtlist, sep_courtlist, oct_courtlist, nov_courtlist, dec_courtlist]

    for mth in months:
        if mth == month:
            courtlist = month_courtlists[months.index(mth)]
            location = ((((day - 1) * 24) + timeslot_index) * 20) + (court_num - 1)
            if courtlist[location].get(1.0, END) == "\n":
                courtlist[location].insert(END, name + '\n')
                courtlist[location].insert(END, number + '\n')
                courtlist[location].insert(END, time_stamp[0] + " - " + time_stamp[1] + '\n')
                courtlist[location].insert(END, "Booking ID: " + str(location) + '\n')
                courtlist[location].config(bg="#00688B", fg="white")
                with open("bookingDataStorage.txt", "a") as f:
                    f.write(name)
                    f.write("\n")
                    f.write(number)
                    f.write("\n")
                    f.write(time_stamp[0])
                    f.write("\n")
                    f.write(str(length_input))
                    f.write("\n")
                    f.write(month + " " + str(day))
                    f.write("\n")
                    f.write('Location Code: ' + str(location))
                    f.write("\n")
                f.close()
            else:
                error_window = Toplevel()
                error_window.geometry("260x85")
                error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
                help_message = Label(error_window, text = 'OVERBOOKING WARNING', fg="black", font=16).pack()
                exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
                error_window.mainloop()

'''Cancellation Function'''
def booking_canceller(month, location): #Cancels bookings and removes them from the employee display.
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_courtlists = [jan_courtlist, feb_courtlist, mar_courtlist, apr_courtlist, may_courtlist, jun_courtlist, jul_courtlist, aug_courtlist, sep_courtlist, oct_courtlist, nov_courtlist, dec_courtlist]
    
    for mth in months:
        if mth == month:
            courtlist = month_courtlists[months.index(mth)]
            if courtlist[location].get(1.0, END) != "\n":
                courtlist[location].delete(1.0, END)
                courtlist[location].config(bg="#008B00")
            else:
                error_window = Toplevel()
                error_window.geometry("260x85")
                error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
                help_message = Label(error_window, text = 'There is no booking to cancel.', fg="black", font=16).pack()
                exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
                courtlist[location].config(bg="#008B00")
                error_window.mainloop()

'''Start-up Booking Loader'''
def startup_insertion(input_name, input_num, location_code, input_month, timings): #Inserts bookings at startup to employee display. 
    code_num = int(location_code.strip('Location Code: '))
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month_courtlists = [jan_courtlist, feb_courtlist, mar_courtlist, apr_courtlist, may_courtlist, jun_courtlist, jul_courtlist, aug_courtlist, sep_courtlist, oct_courtlist, nov_courtlist, dec_courtlist]

    for month in months:
        if month == input_month:
            courtlist = month_courtlists[months.index(month)]
            courtlist[code_num].insert(END, input_name + '\n')
            courtlist[code_num].insert(END, input_num + '\n')
            courtlist[code_num].insert(END, timings[0] + ' - ' + timings[1] + '\n')
            courtlist[code_num].insert(END, "Booking ID: " + location_code.strip('Location Code: ') + '\n')
            courtlist[code_num].config(bg="#00688B", fg="white")
            break

schedule_window.mainloop()
