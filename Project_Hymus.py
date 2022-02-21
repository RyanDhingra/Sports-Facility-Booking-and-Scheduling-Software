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
    img = Image.open(INSERT COMPANY LOGO IMAGE HERE)
    resized_img = img.resize((400, 200), Image.ANTIALIAS)
    logo = ImageTk.PhotoImage(resized_img)
    logo_label = Label(prebooking_window, image=logo).pack()

    '''User Inputs'''
    time_choice_list = ['12AM', '1AM', '2AM', '3AM', '4AM', '5AM', '6AM', '7AM', '8AM', '9AM', '10AM', '11AM', '12PM', '1PM', '2PM', '3PM', '4PM', '5PM', '6PM', '7PM', '8PM', '9PM', '10PM', '11PM', '12AM']
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
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
            
            '''Court Activator'''
            if input_month == "January":
                if "January" not in activated_list:
                    january_courts()
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                    activated_list.append("January")
                else:
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "February":
                if "February" not in activated_list:
                    february_courts()
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                        activated_list.append("February")
                else:
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "March":
                if "March" not in activated_list:
                    march_courts()
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                        activated_list.append("March")
                else:
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month == "April":
                if "April" not in activated_list:
                    april_courts()
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                        activated_list.append("April")
                else:
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month == "May":
                if "May" not in activated_list:
                    may_courts()
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                        activated_list.append("May")
                else:
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "June":
                if "June" not in activated_list:
                    june_courts()
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                        activated_list.append("June")
                else:
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "July":
                if "July" not in activated_list:
                    july_courts()
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                        activated_list.append("July")
                else:
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "August":
                if "August" not in activated_list:
                    august_courts()
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                        activated_list.append("August")
                else:
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "September":
                if "September" not in activated_list:
                    september_courts()
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                        activated_list.append("September")
                else:
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "October":
                if "October" not in activated_list:
                    october_courts()
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                        activated_list.append("October")
                else:
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "November":
                if "November" not in activated_list:
                    november_courts()
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                        activated_list.append("November")
                else:
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "December":
                if "December" not in activated_list:
                    december_courts()
                    for day in day_list:
                        for times in list_of_time_slots:
                            for court in court_num_list:
                                input_courtnum = int(court)
                                input_day = int(day)
                                booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                        activated_list.append("December")
                else:
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

        columnplaceholder = Label(root, text="                                                               ", bg= "lightblue").grid(row = 0, column=0)
        columnplaceholder = Label(root, text="                                                               ", bg= "lightblue").grid(row = 0, column=2)
        columnplaceholder = Label(root, text="                                                               ", bg= "lightblue").grid(row = 0, column=4)
        columnplaceholder = Label(root, text="                                                               ", bg= "lightblue").grid(row = 0, column=6)
        columnplaceholder = Label(root, text="                                                               ", bg= "lightblue").grid(row = 0, column=8)
        
        row_placeholder = Label(root, text=" ", bg= "lightblue").grid(row = 3, column=1)
        row_placeholder = Label(root, text=" ", bg= "lightblue").grid(row = 6, column=1) 
        row_placeholder = Label(root, text=" ", bg= "lightblue").grid(row = 9, column=1) 
        row_placeholder = Label(root, text=" ", bg= "lightblue").grid(row = 12, column=1)

        court_number = Label(root, text="Court 1", bg= "lightblue", font=16).grid(row = 1, column=1)
        court_number = Label(root, text="Court 2", bg= "lightblue", font=16).grid(row = 4, column=1) 
        court_number = Label(root, text="Court 3", bg= "lightblue", font=16).grid(row = 7, column=1) 
        court_number = Label(root, text="Court 4", bg= "lightblue", font=16).grid(row = 10, column=1)
        court_number = Label(root, text="Court 5", bg= "lightblue", font=16).grid(row = 1, column=3)
        court_number = Label(root, text="Court 6", bg= "lightblue", font=16).grid(row = 4, column=3) 
        court_number = Label(root, text="Court 7", bg= "lightblue", font=16).grid(row = 7, column=3) 
        court_number = Label(root, text="Court 8", bg= "lightblue", font=16).grid(row = 10, column=3)
        court_number = Label(root, text="Court 9", bg= "lightblue", font=16).grid(row = 1, column=5)
        court_number = Label(root, text="Court 10", bg= "lightblue", font=16).grid(row = 4, column=5) 
        court_number = Label(root, text="Court 11", bg= "lightblue", font=16).grid(row = 7, column=5) 
        court_number = Label(root, text="Court 12", bg= "lightblue", font=16).grid(row = 10, column=5)
        court_number = Label(root, text="Court 13", bg= "lightblue", font=16).grid(row = 1, column=7)
        court_number = Label(root, text="Court 14", bg= "lightblue", font=16).grid(row = 4, column=7) 
        court_number = Label(root, text="Court 15", bg= "lightblue", font=16).grid(row = 7, column=7) 
        court_number = Label(root, text="Court 16", bg= "lightblue", font=16).grid(row = 10, column=7)
        court_number = Label(root, text="Court 17", bg= "lightblue", font=16).grid(row = 1, column=9)
        court_number = Label(root, text="Court 18", bg= "lightblue", font=16).grid(row = 4, column=9) 
        court_number = Label(root, text="Court 19", bg= "lightblue", font=16).grid(row = 7, column=9) 
        court_number = Label(root, text="Court 20", bg= "lightblue", font=16).grid(row = 10, column=9)

        display_court1 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court1.image_create(END, image=court_bg)
        display_court1.grid(row = 2, column=1)
        display_court2 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court2.image_create(END, image=court_bg)
        display_court2.grid(row = 5, column=1)
        display_court3 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court2.image_create(END, image=court_bg)
        display_court3.grid(row = 8, column=1)
        display_court4 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court4.image_create(END, image=court_bg)
        display_court4.grid(row = 11, column=1)
        display_court5 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court5.image_create(END, image=court_bg)
        display_court5.grid(row = 2, column=3)
        display_court6 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court6.image_create(END, image=court_bg)
        display_court6.grid(row = 5, column=3)
        display_court7 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court7.image_create(END, image=court_bg)
        display_court7.grid(row = 8, column=3)
        display_court8 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court8.image_create(END, image=court_bg)
        display_court8.grid(row = 11, column=3)
        display_court9 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court9.image_create(END, image=court_bg)
        display_court9.grid(row = 2, column=5)
        display_court10 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court10.image_create(END, image=court_bg)
        display_court10.grid(row = 5, column=5)
        display_court11 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court11.image_create(END, image=court_bg)
        display_court11.grid(row = 8, column=5)
        display_court12 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court12.image_create(END, image=court_bg)
        display_court12.grid(row = 11, column=5)
        display_court13 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court13.image_create(END, image=court_bg)
        display_court13.grid(row = 2, column=7)
        display_court14 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court14.image_create(END, image=court_bg)
        display_court14.grid(row = 5, column=7)
        display_court15 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court15.image_create(END, image=court_bg)
        display_court15.grid(row = 8, column=7)
        display_court16 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court16.image_create(END, image=court_bg)
        display_court16.grid(row = 11, column=7)
        display_court17 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court17.image_create(END, image=court_bg)
        display_court17.grid(row = 2, column=9)
        display_court18 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court18.image_create(END, image=court_bg)
        display_court18.grid(row = 5, column=9)
        display_court19 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court19.image_create(END, image=court_bg)
        display_court19.grid(row = 8, column=9)
        display_court20 = Text(root, width=17, height=11, font=16, bg = "#008B00")
        display_court20.image_create(END, image=court_bg)
        display_court20.grid(row = 11, column=9)

        def updater(): #Customer diplay helper funtion.

            current_time = datetime.datetime.now()
            month = current_time.strftime('%m')
            mins = current_time.strftime('%M')
            day = current_time.strftime('%d')
            hour = current_time.strftime('%H')
            secs = current_time.strftime('%S')
            time_delay = ((60 - int(mins)) * 60) - int(secs)

            while list_of_months[int(month) - 1] in activated_list:
                    
                if list_of_months[int(month) - 1] == "January":
                    court1 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20)].get(1.0, END).split('\n')
                    court2 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 1].get(1.0, END).split('\n')
                    court3 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 2].get(1.0, END).split('\n')
                    court4 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 3].get(1.0, END).split('\n')
                    court5 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 4].get(1.0, END).split('\n')
                    court6 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 5].get(1.0, END).split('\n')
                    court7 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 6].get(1.0, END).split('\n')
                    court8 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 7].get(1.0, END).split('\n')
                    court9 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 8].get(1.0, END).split('\n')
                    court10 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 9].get(1.0, END).split('\n')
                    court11 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 10].get(1.0, END).split('\n')
                    court12 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 11].get(1.0, END).split('\n')
                    court13 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 12].get(1.0, END).split('\n')
                    court14 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 13].get(1.0, END).split('\n')
                    court15 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 14].get(1.0, END).split('\n')
                    court16 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 15].get(1.0, END).split('\n')
                    court17 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 16].get(1.0, END).split('\n')
                    court18 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 17].get(1.0, END).split('\n')
                    court19 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 18].get(1.0, END).split('\n')
                    court20 = jan_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 19].get(1.0, END).split('\n')
                    
                    if court1 != ['','']:
                        display_court1.delete(1.0, END)
                        display_court1.insert(END, court1[0] + '\n')
                        display_court1.insert(END, court1[2])
                        display_court1.config(bg='#00688B', fg="white")
                    else:
                        display_court1.delete(1.0, END)
                        display_court1.config(bg="#008B00")
                        display_court1.image_create(END, image=court_bg)
                    if court2 != ['','']:
                        display_court2.delete(1.0, END)
                        display_court2.insert(END, court2[0] + '\n')
                        display_court2.insert(END, court2[2])
                        display_court2.config(bg='#00688B', fg="white")
                    else:
                        display_court2.delete(1.0, END)
                        display_court2.config(bg="#008B00")
                        display_court2.image_create(END, image=court_bg)
                    if court3 != ['','']:
                        display_court3.delete(1.0, END)
                        display_court3.insert(END, court3[0] + '\n')
                        display_court3.insert(END, court3[2])
                        display_court3.config(bg='#00688B', fg="white")
                    else:
                        display_court3.delete(1.0, END)
                        display_court3.config(bg="#008B00")
                        display_court3.image_create(END, image=court_bg)
                    if court4 != ['','']:
                        display_court4.delete(1.0, END)
                        display_court4.insert(END, court4[0] + '\n')
                        display_court4.insert(END, court4[2])
                        display_court4.config(bg='#00688B', fg="white")
                    else:
                        display_court4.delete(1.0, END)
                        display_court4.config(bg="#008B00")
                        display_court4.image_create(END, image=court_bg)
                    if court5 != ['','']:
                        display_court5.delete(1.0, END)
                        display_court5.insert(END, court5[0] + '\n')
                        display_court5.insert(END, court5[2])
                        display_court5.config(bg='#00688B', fg="white")
                    else:
                        display_court5.delete(1.0, END)
                        display_court5.config(bg="#008B00")
                        display_court5.image_create(END, image=court_bg)
                    if court6 != ['','']:
                        display_court6.delete(1.0, END)
                        display_court6.insert(END, court6[0] + '\n')
                        display_court6.insert(END, court6[2])
                        display_court6.config(bg='#00688B', fg="white")
                    else:
                        display_court6.delete(1.0, END)
                        display_court6.config(bg="#008B00")
                        display_court6.image_create(END, image=court_bg)
                    if court7 != ['','']:
                        display_court7.delete(1.0, END)
                        display_court7.insert(END, court7[0] + '\n')
                        display_court7.insert(END, court7[2])
                        display_court7.config(bg='#00688B', fg="white")
                    else:
                        display_court7.delete(1.0, END)
                        display_court7.config(bg="#008B00")
                        display_court7.image_create(END, image=court_bg)
                    if court8 != ['','']:
                        display_court8.delete(1.0, END)
                        display_court8.insert(END, court8[0] + '\n')
                        display_court8.insert(END, court8[2])
                        display_court8.config(bg='#00688B', fg="white")
                    else:
                        display_court8.delete(1.0, END)
                        display_court8.config(bg="#008B00")
                        display_court8.image_create(END, image=court_bg)
                    if court9 != ['','']:
                        display_court9.delete(1.0, END)
                        display_court9.insert(END, court9[0] + '\n')
                        display_court9.insert(END, court9[2])
                        display_court9.config(bg='#00688B', fg="white")
                    else:
                        display_court9.delete(1.0, END)
                        display_court9.config(bg="#008B00")
                        display_court9.image_create(END, image=court_bg)
                    if court10 != ['','']:
                        display_court10.delete(1.0, END)
                        display_court10.insert(END, court10[0] + '\n')
                        display_court10.insert(END, court10[2])
                        display_court10.config(bg='#00688B', fg="white")
                    else:
                        display_court10.delete(1.0, END)
                        display_court10.config(bg="#008B00")
                        display_court10.image_create(END, image=court_bg)
                    if court11 != ['','']:
                        display_court11.delete(1.0, END)
                        display_court11.insert(END, court11[0] + '\n')
                        display_court11.insert(END, court11[2])
                        display_court11.config(bg='#00688B', fg="white")
                    else:
                        display_court11.delete(1.0, END)
                        display_court11.config(bg="#008B00")
                        display_court11.image_create(END, image=court_bg)
                    if court12 != ['','']:
                        display_court12.delete(1.0, END)
                        display_court12.insert(END, court12[0] + '\n')
                        display_court12.insert(END, court12[2])
                        display_court12.config(bg='#00688B', fg="white")
                    else:
                        display_court12.delete(1.0, END)
                        display_court12.config(bg="#008B00")
                        display_court12.image_create(END, image=court_bg)
                    if court13 != ['','']:
                        display_court13.delete(1.0, END)
                        display_court13.insert(END, court13[0] + '\n')
                        display_court13.insert(END, court13[2])
                        display_court13.config(bg='#00688B', fg="white")
                    else:
                        display_court13.delete(1.0, END)
                        display_court13.config(bg="#008B00")
                        display_court13.image_create(END, image=court_bg)
                    if court14 != ['','']:
                        display_court14.delete(1.0, END)
                        display_court14.insert(END, court14[0] + '\n')
                        display_court14.insert(END, court14[2])
                        display_court14.config(bg='#00688B', fg="white")
                    else:
                        display_court14.delete(1.0, END)
                        display_court14.config(bg="#008B00")
                        display_court14.image_create(END, image=court_bg)
                    if court15 != ['','']:
                        display_court15.delete(1.0, END)
                        display_court15.insert(END, court15[0] + '\n')
                        display_court15.insert(END, court15[2])
                        display_court15.config(bg='#00688B', fg="white")
                    else:
                        display_court15.delete(1.0, END)
                        display_court15.config(bg="#008B00")
                        display_court15.image_create(END, image=court_bg)
                    if court16 != ['','']:
                        display_court16.delete(1.0, END)
                        display_court16.insert(END, court16[0] + '\n')
                        display_court16.insert(END, court16[2])
                        display_court16.config(bg='#00688B', fg="white")
                    else:
                        display_court16.delete(1.0, END)
                        display_court16.config(bg="#008B00")
                        display_court16.image_create(END, image=court_bg)
                    if court17 != ['','']:
                        display_court17.delete(1.0, END)
                        display_court17.insert(END, court17[0] + '\n')
                        display_court17.insert(END, court17[2])
                        display_court17.config(bg='#00688B', fg="white")
                    else:
                        display_court17.delete(1.0, END)
                        display_court17.config(bg="#008B00")
                        display_court17.image_create(END, image=court_bg)
                    if court18 != ['','']:
                        display_court18.delete(1.0, END)
                        display_court18.insert(END, court18[0] + '\n')
                        display_court18.insert(END, court18[2])
                        display_court18.config(bg='#00688B', fg="white")
                    else:
                        display_court18.delete(1.0, END)
                        display_court18.config(bg="008B00")
                        display_court18.image_create(END, image=court_bg)
                    if court19 != ['','']:
                        display_court19.delete(1.0, END)
                        display_court19.insert(END, court19[0] + '\n')
                        display_court19.insert(END, court19[2])
                        display_court19.config(bg='#00688B', fg="white")
                    else:
                        display_court19.delete(1.0, END)
                        display_court19.config(bg="#008B00")
                        display_court19.image_create(END, image=court_bg)
                    if court20 != ['','']:
                        display_court20.delete(1.0, END)
                        display_court20.insert(END, court20[0] + '\n')
                        display_court20.insert(END, court20[2])
                        display_court20.config(bg='#00688B', fg="white")
                    else:
                        display_court20.delete(1.0, END)
                        display_court20.config(bg="#008B00")
                        display_court20.image_create(END, image=court_bg)
                
                elif list_of_months[int(month) - 1] == "February":
                    
                    court1 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20)].get(1.0, END).split('\n')
                    court2 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 1].get(1.0, END).split('\n')
                    court3 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 2].get(1.0, END).split('\n')
                    court4 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 3].get(1.0, END).split('\n')
                    court5 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 4].get(1.0, END).split('\n')
                    court6 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 5].get(1.0, END).split('\n')
                    court7 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 6].get(1.0, END).split('\n')
                    court8 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 7].get(1.0, END).split('\n')
                    court9 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 8].get(1.0, END).split('\n')
                    court10 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 9].get(1.0, END).split('\n')
                    court11 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 10].get(1.0, END).split('\n')
                    court12 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 11].get(1.0, END).split('\n')
                    court13 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 12].get(1.0, END).split('\n')
                    court14 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 13].get(1.0, END).split('\n')
                    court15 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 14].get(1.0, END).split('\n')
                    court16 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 15].get(1.0, END).split('\n')
                    court17 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 16].get(1.0, END).split('\n')
                    court18 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 17].get(1.0, END).split('\n')
                    court19 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 18].get(1.0, END).split('\n')
                    court20 = feb_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 19].get(1.0, END).split('\n')
                    
                    if court1 != ['','']:
                        display_court1.delete(1.0, END)
                        display_court1.insert(END, court1[0] + '\n')
                        display_court1.insert(END, court1[2])
                        display_court1.config(bg='#00688B', fg="white")
                    else:
                        display_court1.delete(1.0, END)
                        display_court1.config(bg="#008B00")
                        display_court1.image_create(END, image=court_bg)
                    if court2 != ['','']:
                        display_court2.delete(1.0, END)
                        display_court2.insert(END, court2[0] + '\n')
                        display_court2.insert(END, court2[2])
                        display_court2.config(bg='#00688B', fg="white")
                    else:
                        display_court2.delete(1.0, END)
                        display_court2.config(bg="#008B00")
                        display_court2.image_create(END, image=court_bg)
                    if court3 != ['','']:
                        display_court3.delete(1.0, END)
                        display_court3.insert(END, court3[0] + '\n')
                        display_court3.insert(END, court3[2])
                        display_court3.config(bg='#00688B', fg="white")
                    else:
                        display_court3.delete(1.0, END)
                        display_court3.config(bg="#008B00")
                        display_court3.image_create(END, image=court_bg)
                    if court4 != ['','']:
                        display_court4.delete(1.0, END)
                        display_court4.insert(END, court4[0] + '\n')
                        display_court4.insert(END, court4[2])
                        display_court4.config(bg='#00688B', fg="white")
                    else:
                        display_court4.delete(1.0, END)
                        display_court4.config(bg="#008B00")
                        display_court4.image_create(END, image=court_bg)
                    if court5 != ['','']:
                        display_court5.delete(1.0, END)
                        display_court5.insert(END, court5[0] + '\n')
                        display_court5.insert(END, court5[2])
                        display_court5.config(bg='#00688B', fg="white")
                    else:
                        display_court5.delete(1.0, END)
                        display_court5.config(bg="#008B00")
                        display_court5.image_create(END, image=court_bg)
                    if court6 != ['','']:
                        display_court6.delete(1.0, END)
                        display_court6.insert(END, court6[0] + '\n')
                        display_court6.insert(END, court6[2])
                        display_court6.config(bg='#00688B', fg="white")
                    else:
                        display_court6.delete(1.0, END)
                        display_court6.config(bg="#008B00")
                        display_court6.image_create(END, image=court_bg)
                    if court7 != ['','']:
                        display_court7.delete(1.0, END)
                        display_court7.insert(END, court7[0] + '\n')
                        display_court7.insert(END, court7[2])
                        display_court7.config(bg='#00688B', fg="white")
                    else:
                        display_court7.delete(1.0, END)
                        display_court7.config(bg="#008B00")
                        display_court7.image_create(END, image=court_bg)
                    if court8 != ['','']:
                        display_court8.delete(1.0, END)
                        display_court8.insert(END, court8[0] + '\n')
                        display_court8.insert(END, court8[2])
                        display_court8.config(bg='#00688B', fg="white")
                    else:
                        display_court8.delete(1.0, END)
                        display_court8.config(bg="#008B00")
                        display_court8.image_create(END, image=court_bg)
                    if court9 != ['','']:
                        display_court9.delete(1.0, END)
                        display_court9.insert(END, court9[0] + '\n')
                        display_court9.insert(END, court9[2])
                        display_court9.config(bg='#00688B', fg="white")
                    else:
                        display_court9.delete(1.0, END)
                        display_court9.config(bg="#008B00")
                        display_court9.image_create(END, image=court_bg)
                    if court10 != ['','']:
                        display_court10.delete(1.0, END)
                        display_court10.insert(END, court10[0] + '\n')
                        display_court10.insert(END, court10[2])
                        display_court10.config(bg='#00688B', fg="white")
                    else:
                        display_court10.delete(1.0, END)
                        display_court10.config(bg="#008B00")
                        display_court10.image_create(END, image=court_bg)
                    if court11 != ['','']:
                        display_court11.delete(1.0, END)
                        display_court11.insert(END, court11[0] + '\n')
                        display_court11.insert(END, court11[2])
                        display_court11.config(bg='#00688B', fg="white")
                    else:
                        display_court11.delete(1.0, END)
                        display_court11.config(bg="#008B00")
                        display_court11.image_create(END, image=court_bg)
                    if court12 != ['','']:
                        display_court12.delete(1.0, END)
                        display_court12.insert(END, court12[0] + '\n')
                        display_court12.insert(END, court12[2])
                        display_court12.config(bg='#00688B', fg="white")
                    else:
                        display_court12.delete(1.0, END)
                        display_court12.config(bg="#008B00")
                        display_court12.image_create(END, image=court_bg)
                    if court13 != ['','']:
                        display_court13.delete(1.0, END)
                        display_court13.insert(END, court13[0] + '\n')
                        display_court13.insert(END, court13[2])
                        display_court13.config(bg='#00688B', fg="white")
                    else:
                        display_court13.delete(1.0, END)
                        display_court13.config(bg="#008B00")
                        display_court13.image_create(END, image=court_bg)
                    if court14 != ['','']:
                        display_court14.delete(1.0, END)
                        display_court14.insert(END, court14[0] + '\n')
                        display_court14.insert(END, court14[2])
                        display_court14.config(bg='#00688B', fg="white")
                    else:
                        display_court14.delete(1.0, END)
                        display_court14.config(bg="#008B00")
                        display_court14.image_create(END, image=court_bg)
                    if court15 != ['','']:
                        display_court15.delete(1.0, END)
                        display_court15.insert(END, court15[0] + '\n')
                        display_court15.insert(END, court15[2])
                        display_court15.config(bg='#00688B', fg="white")
                    else:
                        display_court15.delete(1.0, END)
                        display_court15.config(bg="#008B00")
                        display_court15.image_create(END, image=court_bg)
                    if court16 != ['','']:
                        display_court16.delete(1.0, END)
                        display_court16.insert(END, court16[0] + '\n')
                        display_court16.insert(END, court16[2])
                        display_court16.config(bg='#00688B', fg="white")
                    else:
                        display_court16.delete(1.0, END)
                        display_court16.config(bg="#008B00")
                        display_court16.image_create(END, image=court_bg)
                    if court17 != ['','']:
                        display_court17.delete(1.0, END)
                        display_court17.insert(END, court17[0] + '\n')
                        display_court17.insert(END, court17[2])
                        display_court17.config(bg='#00688B', fg="white")
                    else:
                        display_court17.delete(1.0, END)
                        display_court17.config(bg="#008B00")
                        display_court17.image_create(END, image=court_bg)
                    if court18 != ['','']:
                        display_court18.delete(1.0, END)
                        display_court18.insert(END, court18[0] + '\n')
                        display_court18.insert(END, court18[2])
                        display_court18.config(bg='#00688B', fg="white")
                    else:
                        display_court18.delete(1.0, END)
                        display_court18.config(bg="#008B00")
                        display_court18.image_create(END, image=court_bg)
                    if court19 != ['','']:
                        display_court19.delete(1.0, END)
                        display_court19.insert(END, court19[0] + '\n')
                        display_court19.insert(END, court19[2])
                        display_court19.config(bg='#00688B', fg="white")
                    else:
                        display_court19.delete(1.0, END)
                        display_court19.config(bg="#008B00")
                        display_court19.image_create(END, image=court_bg)
                    if court20 != ['','']:
                        display_court20.delete(1.0, END)
                        display_court20.insert(END, court20[0] + '\n')
                        display_court20.insert(END, court20[2])
                        display_court20.config(bg='#00688B', fg="white")
                    else:
                        display_court20.delete(1.0, END)
                        display_court20.config(bg="#008B00")
                        display_court20.image_create(END, image=court_bg)
                    
                elif list_of_months[int(month) - 1] == "March":
                    court1 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20)].get(1.0, END).split('\n')
                    court2 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 2].get(1.0, END).split('\n')
                    court3 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 3].get(1.0, END).split('\n')
                    court4 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 4].get(1.0, END).split('\n')
                    court5 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 5].get(1.0, END).split('\n')
                    court6 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 6].get(1.0, END).split('\n')
                    court7 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 7].get(1.0, END).split('\n')
                    court8 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 8].get(1.0, END).split('\n')
                    court9 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 9].get(1.0, END).split('\n')
                    court10 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 10].get(1.0, END).split('\n')
                    court11 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 11].get(1.0, END).split('\n')
                    court12 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 12].get(1.0, END).split('\n')
                    court13 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 13].get(1.0, END).split('\n')
                    court14 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 14].get(1.0, END).split('\n')
                    court15 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 15].get(1.0, END).split('\n')
                    court16 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 16].get(1.0, END).split('\n')
                    court17 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 17].get(1.0, END).split('\n')
                    court18 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 18].get(1.0, END).split('\n')
                    court19 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 19].get(1.0, END).split('\n')
                    court20 = mar_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 20].get(1.0, END).split('\n')

                    if court1 != ['','']:
                        display_court1.delete(1.0, END)
                        display_court1.insert(END, court1[0] + '\n')
                        display_court1.insert(END, court1[2])
                        display_court1.config(bg='#00688B', fg="white")
                    else:
                        display_court1.delete(1.0, END)
                        display_court1.config(bg="#008B00")
                        display_court1.image_create(END, image=court_bg)
                    if court2 != ['','']:
                        display_court2.delete(1.0, END)
                        display_court2.insert(END, court2[0] + '\n')
                        display_court2.insert(END, court2[2])
                        display_court2.config(bg='#00688B', fg="white")
                    else:
                        display_court2.delete(1.0, END)
                        display_court2.config(bg="#008B00")
                        display_court2.image_create(END, image=court_bg)
                    if court3 != ['','']:
                        display_court3.delete(1.0, END)
                        display_court3.insert(END, court3[0] + '\n')
                        display_court3.insert(END, court3[2])
                        display_court3.config(bg='#00688B', fg="white")
                    else:
                        display_court3.delete(1.0, END)
                        display_court3.config(bg="#008B00")
                        display_court3.image_create(END, image=court_bg)
                    if court4 != ['','']:
                        display_court4.delete(1.0, END)
                        display_court4.insert(END, court4[0] + '\n')
                        display_court4.insert(END, court4[2])
                        display_court4.config(bg='#00688B', fg="white")
                    else:
                        display_court4.delete(1.0, END)
                        display_court4.config(bg="#008B00")
                        display_court4.image_create(END, image=court_bg)
                    if court5 != ['','']:
                        display_court5.delete(1.0, END)
                        display_court5.insert(END, court5[0] + '\n')
                        display_court5.insert(END, court5[2])
                        display_court5.config(bg='#00688B', fg="white")
                    else:
                        display_court5.delete(1.0, END)
                        display_court5.config(bg="#008B00")
                        display_court5.image_create(END, image=court_bg)
                    if court6 != ['','']:
                        display_court6.delete(1.0, END)
                        display_court6.insert(END, court6[0] + '\n')
                        display_court6.insert(END, court6[2])
                        display_court6.config(bg='#00688B', fg="white")
                    else:
                        display_court6.delete(1.0, END)
                        display_court6.config(bg="#008B00")
                        display_court6.image_create(END, image=court_bg)
                    if court7 != ['','']:
                        display_court7.delete(1.0, END)
                        display_court7.insert(END, court7[0] + '\n')
                        display_court7.insert(END, court7[2])
                        display_court7.config(bg='#00688B', fg="white")
                    else:
                        display_court7.delete(1.0, END)
                        display_court7.config(bg="#008B00")
                        display_court7.image_create(END, image=court_bg)
                    if court8 != ['','']:
                        display_court8.delete(1.0, END)
                        display_court8.insert(END, court8[0] + '\n')
                        display_court8.insert(END, court8[2])
                        display_court8.config(bg='#00688B', fg="white")
                    else:
                        display_court8.delete(1.0, END)
                        display_court8.config(bg="#008B00")
                        display_court8.image_create(END, image=court_bg)
                    if court9 != ['','']:
                        display_court9.delete(1.0, END)
                        display_court9.insert(END, court9[0] + '\n')
                        display_court9.insert(END, court9[2])
                        display_court9.config(bg='#00688B', fg="white")
                    else:
                        display_court9.delete(1.0, END)
                        display_court9.config(bg="#008B00")
                        display_court9.image_create(END, image=court_bg)
                    if court10 != ['','']:
                        display_court10.delete(1.0, END)
                        display_court10.insert(END, court10[0] + '\n')
                        display_court10.insert(END, court10[2])
                        display_court10.config(bg='#00688B', fg="white")
                    else:
                        display_court10.delete(1.0, END)
                        display_court10.config(bg="#008B00")
                        display_court10.image_create(END, image=court_bg)
                    if court11 != ['','']:
                        display_court11.delete(1.0, END)
                        display_court11.insert(END, court11[0] + '\n')
                        display_court11.insert(END, court11[2])
                        display_court11.config(bg='#00688B', fg="white")
                    else:
                        display_court11.delete(1.0, END)
                        display_court11.config(bg="#008B00")
                        display_court11.image_create(END, image=court_bg)
                    if court12 != ['','']:
                        display_court12.delete(1.0, END)
                        display_court12.insert(END, court12[0] + '\n')
                        display_court12.insert(END, court12[2])
                        display_court12.config(bg='#00688B', fg="white")
                    else:
                        display_court12.delete(1.0, END)
                        display_court12.config(bg="#008B00")
                        display_court12.image_create(END, image=court_bg)
                    if court13 != ['','']:
                        display_court13.delete(1.0, END)
                        display_court13.insert(END, court13[0] + '\n')
                        display_court13.insert(END, court13[2])
                        display_court13.config(bg='#00688B', fg="white")
                    else:
                        display_court13.delete(1.0, END)
                        display_court13.config(bg="#008B00")
                        display_court13.image_create(END, image=court_bg)
                    if court14 != ['','']:
                        display_court14.delete(1.0, END)
                        display_court14.insert(END, court14[0] + '\n')
                        display_court14.insert(END, court14[2])
                        display_court14.config(bg='#00688B', fg="white")
                    else:
                        display_court14.delete(1.0, END)
                        display_court14.config(bg="#008B00")
                        display_court14.image_create(END, image=court_bg)
                    if court15 != ['','']:
                        display_court15.delete(1.0, END)
                        display_court15.insert(END, court15[0] + '\n')
                        display_court15.insert(END, court15[2])
                        display_court15.config(bg='#00688B', fg="white")
                    else:
                        display_court15.delete(1.0, END)
                        display_court15.config(bg="#008B00")
                        display_court15.image_create(END, image=court_bg)
                    if court16 != ['','']:
                        display_court16.delete(1.0, END)
                        display_court16.insert(END, court16[0] + '\n')
                        display_court16.insert(END, court16[2])
                        display_court16.config(bg='#00688B', fg="white")
                    else:
                        display_court16.delete(1.0, END)
                        display_court16.config(bg="#008B00")
                        display_court16.image_create(END, image=court_bg)
                    if court17 != ['','']:
                        display_court17.delete(1.0, END)
                        display_court17.insert(END, court17[0] + '\n')
                        display_court17.insert(END, court17[2])
                        display_court17.config(bg='#00688B', fg="white")
                    else:
                        display_court17.delete(1.0, END)
                        display_court17.config(bg="#008B00")
                        display_court17.image_create(END, image=court_bg)
                    if court18 != ['','']:
                        display_court18.delete(1.0, END)
                        display_court18.insert(END, court18[0] + '\n')
                        display_court18.insert(END, court18[2])
                        display_court18.config(bg='#00688B', fg="white")
                    else:
                        display_court18.delete(1.0, END)
                        display_court18.config(bg="008B00")
                        display_court18.image_create(END, image=court_bg)
                    if court19 != ['','']:
                        display_court19.delete(1.0, END)
                        display_court19.insert(END, court19[0] + '\n')
                        display_court19.insert(END, court19[2])
                        display_court19.config(bg='#00688B', fg="white")
                    else:
                        display_court19.delete(1.0, END)
                        display_court19.config(bg="#008B00")
                        display_court19.image_create(END, image=court_bg)
                    if court20 != ['','']:
                        display_court20.delete(1.0, END)
                        display_court20.insert(END, court20[0] + '\n')
                        display_court20.insert(END, court20[2])
                        display_court20.config(bg='#00688B', fg="white")
                    else:
                        display_court20.delete(1.0, END)
                        display_court20.config(bg="#008B00")
                        display_court20.image_create(END, image=court_bg)
                
                elif list_of_months[int(month) - 1] == "April":
                    court1 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20)].get(1.0, END).split('\n')
                    court2 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 2].get(1.0, END).split('\n')
                    court3 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 3].get(1.0, END).split('\n')
                    court4 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 4].get(1.0, END).split('\n')
                    court5 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 5].get(1.0, END).split('\n')
                    court6 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 6].get(1.0, END).split('\n')
                    court7 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 7].get(1.0, END).split('\n')
                    court8 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 8].get(1.0, END).split('\n')
                    court9 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 9].get(1.0, END).split('\n')
                    court10 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 10].get(1.0, END).split('\n')
                    court11 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 11].get(1.0, END).split('\n')
                    court12 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 12].get(1.0, END).split('\n')
                    court13 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 13].get(1.0, END).split('\n')
                    court14 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 14].get(1.0, END).split('\n')
                    court15 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 15].get(1.0, END).split('\n')
                    court16 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 16].get(1.0, END).split('\n')
                    court17 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 17].get(1.0, END).split('\n')
                    court18 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 18].get(1.0, END).split('\n')
                    court19 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 19].get(1.0, END).split('\n')
                    court20 = apr_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 20].get(1.0, END).split('\n')

                    if court1 != ['','']:
                        display_court1.delete(1.0, END)
                        display_court1.insert(END, court1[0] + '\n')
                        display_court1.insert(END, court1[2])
                        display_court1.config(bg='#00688B', fg="white")
                    else:
                        display_court1.delete(1.0, END)
                        display_court1.config(bg="#008B00")
                        display_court1.image_create(END, image=court_bg)
                    if court2 != ['','']:
                        display_court2.delete(1.0, END)
                        display_court2.insert(END, court2[0] + '\n')
                        display_court2.insert(END, court2[2])
                        display_court2.config(bg='#00688B', fg="white")
                    else:
                        display_court2.delete(1.0, END)
                        display_court2.config(bg="#008B00")
                        display_court2.image_create(END, image=court_bg)
                    if court3 != ['','']:
                        display_court3.delete(1.0, END)
                        display_court3.insert(END, court3[0] + '\n')
                        display_court3.insert(END, court3[2])
                        display_court3.config(bg='#00688B', fg="white")
                    else:
                        display_court3.delete(1.0, END)
                        display_court3.config(bg="#008B00")
                        display_court3.image_create(END, image=court_bg)
                    if court4 != ['','']:
                        display_court4.delete(1.0, END)
                        display_court4.insert(END, court4[0] + '\n')
                        display_court4.insert(END, court4[2])
                        display_court4.config(bg='#00688B', fg="white")
                    else:
                        display_court4.delete(1.0, END)
                        display_court4.config(bg="#008B00")
                        display_court4.image_create(END, image=court_bg)
                    if court5 != ['','']:
                        display_court5.delete(1.0, END)
                        display_court5.insert(END, court5[0] + '\n')
                        display_court5.insert(END, court5[2])
                        display_court5.config(bg='#00688B', fg="white")
                    else:
                        display_court5.delete(1.0, END)
                        display_court5.config(bg="#008B00")
                        display_court5.image_create(END, image=court_bg)
                    if court6 != ['','']:
                        display_court6.delete(1.0, END)
                        display_court6.insert(END, court6[0] + '\n')
                        display_court6.insert(END, court6[2])
                        display_court6.config(bg='#00688B', fg="white")
                    else:
                        display_court6.delete(1.0, END)
                        display_court6.config(bg="#008B00")
                        display_court6.image_create(END, image=court_bg)
                    if court7 != ['','']:
                        display_court7.delete(1.0, END)
                        display_court7.insert(END, court7[0] + '\n')
                        display_court7.insert(END, court7[2])
                        display_court7.config(bg='#00688B', fg="white")
                    else:
                        display_court7.delete(1.0, END)
                        display_court7.config(bg="#008B00")
                        display_court7.image_create(END, image=court_bg)
                    if court8 != ['','']:
                        display_court8.delete(1.0, END)
                        display_court8.insert(END, court8[0] + '\n')
                        display_court8.insert(END, court8[2])
                        display_court8.config(bg='#00688B', fg="white")
                    else:
                        display_court8.delete(1.0, END)
                        display_court8.config(bg="#008B00")
                        display_court8.image_create(END, image=court_bg)
                    if court9 != ['','']:
                        display_court9.delete(1.0, END)
                        display_court9.insert(END, court9[0] + '\n')
                        display_court9.insert(END, court9[2])
                        display_court9.config(bg='#00688B', fg="white")
                    else:
                        display_court9.delete(1.0, END)
                        display_court9.config(bg="#008B00")
                        display_court9.image_create(END, image=court_bg)
                    if court10 != ['','']:
                        display_court10.delete(1.0, END)
                        display_court10.insert(END, court10[0] + '\n')
                        display_court10.insert(END, court10[2])
                        display_court10.config(bg='#00688B', fg="white")
                    else:
                        display_court10.delete(1.0, END)
                        display_court10.config(bg="#008B00")
                        display_court10.image_create(END, image=court_bg)
                    if court11 != ['','']:
                        display_court11.delete(1.0, END)
                        display_court11.insert(END, court11[0] + '\n')
                        display_court11.insert(END, court11[2])
                        display_court11.config(bg='#00688B', fg="white")
                    else:
                        display_court11.delete(1.0, END)
                        display_court11.config(bg="#008B00")
                        display_court11.image_create(END, image=court_bg)
                    if court12 != ['','']:
                        display_court12.delete(1.0, END)
                        display_court12.insert(END, court12[0] + '\n')
                        display_court12.insert(END, court12[2])
                        display_court12.config(bg='#00688B', fg="white")
                    else:
                        display_court12.delete(1.0, END)
                        display_court12.config(bg="#008B00")
                        display_court12.image_create(END, image=court_bg)
                    if court13 != ['','']:
                        display_court13.delete(1.0, END)
                        display_court13.insert(END, court13[0] + '\n')
                        display_court13.insert(END, court13[2])
                        display_court13.config(bg='#00688B', fg="white")
                    else:
                        display_court13.delete(1.0, END)
                        display_court13.config(bg="#008B00")
                        display_court13.image_create(END, image=court_bg)
                    if court14 != ['','']:
                        display_court14.delete(1.0, END)
                        display_court14.insert(END, court14[0] + '\n')
                        display_court14.insert(END, court14[2])
                        display_court14.config(bg='#00688B', fg="white")
                    else:
                        display_court14.delete(1.0, END)
                        display_court14.config(bg="#008B00")
                        display_court14.image_create(END, image=court_bg)
                    if court15 != ['','']:
                        display_court15.delete(1.0, END)
                        display_court15.insert(END, court15[0] + '\n')
                        display_court15.insert(END, court15[2])
                        display_court15.config(bg='#00688B', fg="white")
                    else:
                        display_court15.delete(1.0, END)
                        display_court15.config(bg="#008B00")
                        display_court15.image_create(END, image=court_bg)
                    if court16 != ['','']:
                        display_court16.delete(1.0, END)
                        display_court16.insert(END, court16[0] + '\n')
                        display_court16.insert(END, court16[2])
                        display_court16.config(bg='#00688B', fg="white")
                    else:
                        display_court16.delete(1.0, END)
                        display_court16.config(bg="#008B00")
                        display_court16.image_create(END, image=court_bg)
                    if court17 != ['','']:
                        display_court17.delete(1.0, END)
                        display_court17.insert(END, court17[0] + '\n')
                        display_court17.insert(END, court17[2])
                        display_court17.config(bg='#00688B', fg="white")
                    else:
                        display_court17.delete(1.0, END)
                        display_court17.config(bg="#008B00")
                        display_court17.image_create(END, image=court_bg)
                    if court18 != ['','']:
                        display_court18.delete(1.0, END)
                        display_court18.insert(END, court18[0] + '\n')
                        display_court18.insert(END, court18[2])
                        display_court18.config(bg='#00688B', fg="white")
                    else:
                        display_court18.delete(1.0, END)
                        display_court18.config(bg="008B00")
                        display_court18.image_create(END, image=court_bg)
                    if court19 != ['','']:
                        display_court19.delete(1.0, END)
                        display_court19.insert(END, court19[0] + '\n')
                        display_court19.insert(END, court19[2])
                        display_court19.config(bg='#00688B', fg="white")
                    else:
                        display_court19.delete(1.0, END)
                        display_court19.config(bg="#008B00")
                        display_court19.image_create(END, image=court_bg)
                    if court20 != ['','']:
                        display_court20.delete(1.0, END)
                        display_court20.insert(END, court20[0] + '\n')
                        display_court20.insert(END, court20[2])
                        display_court20.config(bg='#00688B', fg="white")
                    else:
                        display_court20.delete(1.0, END)
                        display_court20.config(bg="#008B00")
                        display_court20.image_create(END, image=court_bg)
                
                elif list_of_months[int(month) - 1] == "May":
                    court1 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20)].get(1.0, END).split('\n')
                    court2 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 2].get(1.0, END).split('\n')
                    court3 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 3].get(1.0, END).split('\n')
                    court4 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 4].get(1.0, END).split('\n')
                    court5 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 5].get(1.0, END).split('\n')
                    court6 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 6].get(1.0, END).split('\n')
                    court7 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 7].get(1.0, END).split('\n')
                    court8 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 8].get(1.0, END).split('\n')
                    court9 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 9].get(1.0, END).split('\n')
                    court10 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 10].get(1.0, END).split('\n')
                    court11 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 11].get(1.0, END).split('\n')
                    court12 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 12].get(1.0, END).split('\n')
                    court13 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 13].get(1.0, END).split('\n')
                    court14 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 14].get(1.0, END).split('\n')
                    court15 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 15].get(1.0, END).split('\n')
                    court16 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 16].get(1.0, END).split('\n')
                    court17 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 17].get(1.0, END).split('\n')
                    court18 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 18].get(1.0, END).split('\n')
                    court19 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 19].get(1.0, END).split('\n')
                    court20 = may_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 20].get(1.0, END).split('\n')
                    
                    if court1 != ['','']:
                        display_court1.delete(1.0, END)
                        display_court1.insert(END, court1[0] + '\n')
                        display_court1.insert(END, court1[2])
                        display_court1.config(bg='#00688B', fg="white")
                    else:
                        display_court1.delete(1.0, END)
                        display_court1.config(bg="#008B00")
                        display_court1.image_create(END, image=court_bg)
                    if court2 != ['','']:
                        display_court2.delete(1.0, END)
                        display_court2.insert(END, court2[0] + '\n')
                        display_court2.insert(END, court2[2])
                        display_court2.config(bg='#00688B', fg="white")
                    else:
                        display_court2.delete(1.0, END)
                        display_court2.config(bg="#008B00")
                        display_court2.image_create(END, image=court_bg)
                    if court3 != ['','']:
                        display_court3.delete(1.0, END)
                        display_court3.insert(END, court3[0] + '\n')
                        display_court3.insert(END, court3[2])
                        display_court3.config(bg='#00688B', fg="white")
                    else:
                        display_court3.delete(1.0, END)
                        display_court3.config(bg="#008B00")
                        display_court3.image_create(END, image=court_bg)
                    if court4 != ['','']:
                        display_court4.delete(1.0, END)
                        display_court4.insert(END, court4[0] + '\n')
                        display_court4.insert(END, court4[2])
                        display_court4.config(bg='#00688B', fg="white")
                    else:
                        display_court4.delete(1.0, END)
                        display_court4.config(bg="#008B00")
                        display_court4.image_create(END, image=court_bg)
                    if court5 != ['','']:
                        display_court5.delete(1.0, END)
                        display_court5.insert(END, court5[0] + '\n')
                        display_court5.insert(END, court5[2])
                        display_court5.config(bg='#00688B', fg="white")
                    else:
                        display_court5.delete(1.0, END)
                        display_court5.config(bg="#008B00")
                        display_court5.image_create(END, image=court_bg)
                    if court6 != ['','']:
                        display_court6.delete(1.0, END)
                        display_court6.insert(END, court6[0] + '\n')
                        display_court6.insert(END, court6[2])
                        display_court6.config(bg='#00688B', fg="white")
                    else:
                        display_court6.delete(1.0, END)
                        display_court6.config(bg="#008B00")
                        display_court6.image_create(END, image=court_bg)
                    if court7 != ['','']:
                        display_court7.delete(1.0, END)
                        display_court7.insert(END, court7[0] + '\n')
                        display_court7.insert(END, court7[2])
                        display_court7.config(bg='#00688B', fg="white")
                    else:
                        display_court7.delete(1.0, END)
                        display_court7.config(bg="#008B00")
                        display_court7.image_create(END, image=court_bg)
                    if court8 != ['','']:
                        display_court8.delete(1.0, END)
                        display_court8.insert(END, court8[0] + '\n')
                        display_court8.insert(END, court8[2])
                        display_court8.config(bg='#00688B', fg="white")
                    else:
                        display_court8.delete(1.0, END)
                        display_court8.config(bg="#008B00")
                        display_court8.image_create(END, image=court_bg)
                    if court9 != ['','']:
                        display_court9.delete(1.0, END)
                        display_court9.insert(END, court9[0] + '\n')
                        display_court9.insert(END, court9[2])
                        display_court9.config(bg='#00688B', fg="white")
                    else:
                        display_court9.delete(1.0, END)
                        display_court9.config(bg="#008B00")
                        display_court9.image_create(END, image=court_bg)
                    if court10 != ['','']:
                        display_court10.delete(1.0, END)
                        display_court10.insert(END, court10[0] + '\n')
                        display_court10.insert(END, court10[2])
                        display_court10.config(bg='#00688B', fg="white")
                    else:
                        display_court10.delete(1.0, END)
                        display_court10.config(bg="#008B00")
                        display_court10.image_create(END, image=court_bg)
                    if court11 != ['','']:
                        display_court11.delete(1.0, END)
                        display_court11.insert(END, court11[0] + '\n')
                        display_court11.insert(END, court11[2])
                        display_court11.config(bg='#00688B', fg="white")
                    else:
                        display_court11.delete(1.0, END)
                        display_court11.config(bg="#008B00")
                        display_court11.image_create(END, image=court_bg)
                    if court12 != ['','']:
                        display_court12.delete(1.0, END)
                        display_court12.insert(END, court12[0] + '\n')
                        display_court12.insert(END, court12[2])
                        display_court12.config(bg='#00688B', fg="white")
                    else:
                        display_court12.delete(1.0, END)
                        display_court12.config(bg="#008B00")
                        display_court12.image_create(END, image=court_bg)
                    if court13 != ['','']:
                        display_court13.delete(1.0, END)
                        display_court13.insert(END, court13[0] + '\n')
                        display_court13.insert(END, court13[2])
                        display_court13.config(bg='#00688B', fg="white")
                    else:
                        display_court13.delete(1.0, END)
                        display_court13.config(bg="#008B00")
                        display_court13.image_create(END, image=court_bg)
                    if court14 != ['','']:
                        display_court14.delete(1.0, END)
                        display_court14.insert(END, court14[0] + '\n')
                        display_court14.insert(END, court14[2])
                        display_court14.config(bg='#00688B', fg="white")
                    else:
                        display_court14.delete(1.0, END)
                        display_court14.config(bg="#008B00")
                        display_court14.image_create(END, image=court_bg)
                    if court15 != ['','']:
                        display_court15.delete(1.0, END)
                        display_court15.insert(END, court15[0] + '\n')
                        display_court15.insert(END, court15[2])
                        display_court15.config(bg='#00688B', fg="white")
                    else:
                        display_court15.delete(1.0, END)
                        display_court15.config(bg="#008B00")
                        display_court15.image_create(END, image=court_bg)
                    if court16 != ['','']:
                        display_court16.delete(1.0, END)
                        display_court16.insert(END, court16[0] + '\n')
                        display_court16.insert(END, court16[2])
                        display_court16.config(bg='#00688B', fg="white")
                    else:
                        display_court16.delete(1.0, END)
                        display_court16.config(bg="#008B00")
                        display_court16.image_create(END, image=court_bg)
                    if court17 != ['','']:
                        display_court17.delete(1.0, END)
                        display_court17.insert(END, court17[0] + '\n')
                        display_court17.insert(END, court17[2])
                        display_court17.config(bg='#00688B', fg="white")
                    else:
                        display_court17.delete(1.0, END)
                        display_court17.config(bg="#008B00")
                        display_court17.image_create(END, image=court_bg)
                    if court18 != ['','']:
                        display_court18.delete(1.0, END)
                        display_court18.insert(END, court18[0] + '\n')
                        display_court18.insert(END, court18[2])
                        display_court18.config(bg='#00688B', fg="white")
                    else:
                        display_court18.delete(1.0, END)
                        display_court18.config(bg="008B00")
                        display_court18.image_create(END, image=court_bg)
                    if court19 != ['','']:
                        display_court19.delete(1.0, END)
                        display_court19.insert(END, court19[0] + '\n')
                        display_court19.insert(END, court19[2])
                        display_court19.config(bg='#00688B', fg="white")
                    else:
                        display_court19.delete(1.0, END)
                        display_court19.config(bg="#008B00")
                        display_court19.image_create(END, image=court_bg)
                    if court20 != ['','']:
                        display_court20.delete(1.0, END)
                        display_court20.insert(END, court20[0] + '\n')
                        display_court20.insert(END, court20[2])
                        display_court20.config(bg='#00688B', fg="white")
                    else:
                        display_court20.delete(1.0, END)
                        display_court20.config(bg="#008B00")
                        display_court20.image_create(END, image=court_bg)

                elif list_of_months[int(month) - 1] == "June":
                    court1 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20)].get(1.0, END).split('\n')
                    court2 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 2].get(1.0, END).split('\n')
                    court3 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 3].get(1.0, END).split('\n')
                    court4 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 4].get(1.0, END).split('\n')
                    court5 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 5].get(1.0, END).split('\n')
                    court6 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 6].get(1.0, END).split('\n')
                    court7 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 7].get(1.0, END).split('\n')
                    court8 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 8].get(1.0, END).split('\n')
                    court9 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 9].get(1.0, END).split('\n')
                    court10 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 10].get(1.0, END).split('\n')
                    court11 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 11].get(1.0, END).split('\n')
                    court12 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 12].get(1.0, END).split('\n')
                    court13 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 13].get(1.0, END).split('\n')
                    court14 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 14].get(1.0, END).split('\n')
                    court15 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 15].get(1.0, END).split('\n')
                    court16 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 16].get(1.0, END).split('\n')
                    court17 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 17].get(1.0, END).split('\n')
                    court18 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 18].get(1.0, END).split('\n')
                    court19 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 19].get(1.0, END).split('\n')
                    court20 = jun_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 20].get(1.0, END).split('\n')

                    if court1 != ['','']:
                        display_court1.delete(1.0, END)
                        display_court1.insert(END, court1[0] + '\n')
                        display_court1.insert(END, court1[2])
                        display_court1.config(bg='#00688B', fg="white")
                    else:
                        display_court1.delete(1.0, END)
                        display_court1.config(bg="#008B00")
                        display_court1.image_create(END, image=court_bg)
                    if court2 != ['','']:
                        display_court2.delete(1.0, END)
                        display_court2.insert(END, court2[0] + '\n')
                        display_court2.insert(END, court2[2])
                        display_court2.config(bg='#00688B', fg="white")
                    else:
                        display_court2.delete(1.0, END)
                        display_court2.config(bg="#008B00")
                        display_court2.image_create(END, image=court_bg)
                    if court3 != ['','']:
                        display_court3.delete(1.0, END)
                        display_court3.insert(END, court3[0] + '\n')
                        display_court3.insert(END, court3[2])
                        display_court3.config(bg='#00688B', fg="white")
                    else:
                        display_court3.delete(1.0, END)
                        display_court3.config(bg="#008B00")
                        display_court3.image_create(END, image=court_bg)
                    if court4 != ['','']:
                        display_court4.delete(1.0, END)
                        display_court4.insert(END, court4[0] + '\n')
                        display_court4.insert(END, court4[2])
                        display_court4.config(bg='#00688B', fg="white")
                    else:
                        display_court4.delete(1.0, END)
                        display_court4.config(bg="#008B00")
                        display_court4.image_create(END, image=court_bg)
                    if court5 != ['','']:
                        display_court5.delete(1.0, END)
                        display_court5.insert(END, court5[0] + '\n')
                        display_court5.insert(END, court5[2])
                        display_court5.config(bg='#00688B', fg="white")
                    else:
                        display_court5.delete(1.0, END)
                        display_court5.config(bg="#008B00")
                        display_court5.image_create(END, image=court_bg)
                    if court6 != ['','']:
                        display_court6.delete(1.0, END)
                        display_court6.insert(END, court6[0] + '\n')
                        display_court6.insert(END, court6[2])
                        display_court6.config(bg='#00688B', fg="white")
                    else:
                        display_court6.delete(1.0, END)
                        display_court6.config(bg="#008B00")
                        display_court6.image_create(END, image=court_bg)
                    if court7 != ['','']:
                        display_court7.delete(1.0, END)
                        display_court7.insert(END, court7[0] + '\n')
                        display_court7.insert(END, court7[2])
                        display_court7.config(bg='#00688B', fg="white")
                    else:
                        display_court7.delete(1.0, END)
                        display_court7.config(bg="#008B00")
                        display_court7.image_create(END, image=court_bg)
                    if court8 != ['','']:
                        display_court8.delete(1.0, END)
                        display_court8.insert(END, court8[0] + '\n')
                        display_court8.insert(END, court8[2])
                        display_court8.config(bg='#00688B', fg="white")
                    else:
                        display_court8.delete(1.0, END)
                        display_court8.config(bg="#008B00")
                        display_court8.image_create(END, image=court_bg)
                    if court9 != ['','']:
                        display_court9.delete(1.0, END)
                        display_court9.insert(END, court9[0] + '\n')
                        display_court9.insert(END, court9[2])
                        display_court9.config(bg='#00688B', fg="white")
                    else:
                        display_court9.delete(1.0, END)
                        display_court9.config(bg="#008B00")
                        display_court9.image_create(END, image=court_bg)
                    if court10 != ['','']:
                        display_court10.delete(1.0, END)
                        display_court10.insert(END, court10[0] + '\n')
                        display_court10.insert(END, court10[2])
                        display_court10.config(bg='#00688B', fg="white")
                    else:
                        display_court10.delete(1.0, END)
                        display_court10.config(bg="#008B00")
                        display_court10.image_create(END, image=court_bg)
                    if court11 != ['','']:
                        display_court11.delete(1.0, END)
                        display_court11.insert(END, court11[0] + '\n')
                        display_court11.insert(END, court11[2])
                        display_court11.config(bg='#00688B', fg="white")
                    else:
                        display_court11.delete(1.0, END)
                        display_court11.config(bg="#008B00")
                        display_court11.image_create(END, image=court_bg)
                    if court12 != ['','']:
                        display_court12.delete(1.0, END)
                        display_court12.insert(END, court12[0] + '\n')
                        display_court12.insert(END, court12[2])
                        display_court12.config(bg='#00688B', fg="white")
                    else:
                        display_court12.delete(1.0, END)
                        display_court12.config(bg="#008B00")
                        display_court12.image_create(END, image=court_bg)
                    if court13 != ['','']:
                        display_court13.delete(1.0, END)
                        display_court13.insert(END, court13[0] + '\n')
                        display_court13.insert(END, court13[2])
                        display_court13.config(bg='#00688B', fg="white")
                    else:
                        display_court13.delete(1.0, END)
                        display_court13.config(bg="#008B00")
                        display_court13.image_create(END, image=court_bg)
                    if court14 != ['','']:
                        display_court14.delete(1.0, END)
                        display_court14.insert(END, court14[0] + '\n')
                        display_court14.insert(END, court14[2])
                        display_court14.config(bg='#00688B', fg="white")
                    else:
                        display_court14.delete(1.0, END)
                        display_court14.config(bg="#008B00")
                        display_court14.image_create(END, image=court_bg)
                    if court15 != ['','']:
                        display_court15.delete(1.0, END)
                        display_court15.insert(END, court15[0] + '\n')
                        display_court15.insert(END, court15[2])
                        display_court15.config(bg='#00688B', fg="white")
                    else:
                        display_court15.delete(1.0, END)
                        display_court15.config(bg="#008B00")
                        display_court15.image_create(END, image=court_bg)
                    if court16 != ['','']:
                        display_court16.delete(1.0, END)
                        display_court16.insert(END, court16[0] + '\n')
                        display_court16.insert(END, court16[2])
                        display_court16.config(bg='#00688B', fg="white")
                    else:
                        display_court16.delete(1.0, END)
                        display_court16.config(bg="#008B00")
                        display_court16.image_create(END, image=court_bg)
                    if court17 != ['','']:
                        display_court17.delete(1.0, END)
                        display_court17.insert(END, court17[0] + '\n')
                        display_court17.insert(END, court17[2])
                        display_court17.config(bg='#00688B', fg="white")
                    else:
                        display_court17.delete(1.0, END)
                        display_court17.config(bg="#008B00")
                        display_court17.image_create(END, image=court_bg)
                    if court18 != ['','']:
                        display_court18.delete(1.0, END)
                        display_court18.insert(END, court18[0] + '\n')
                        display_court18.insert(END, court18[2])
                        display_court18.config(bg='#00688B', fg="white")
                    else:
                        display_court18.delete(1.0, END)
                        display_court18.config(bg="008B00")
                        display_court18.image_create(END, image=court_bg)
                    if court19 != ['','']:
                        display_court19.delete(1.0, END)
                        display_court19.insert(END, court19[0] + '\n')
                        display_court19.insert(END, court19[2])
                        display_court19.config(bg='#00688B', fg="white")
                    else:
                        display_court19.delete(1.0, END)
                        display_court19.config(bg="#008B00")
                        display_court19.image_create(END, image=court_bg)
                    if court20 != ['','']:
                        display_court20.delete(1.0, END)
                        display_court20.insert(END, court20[0] + '\n')
                        display_court20.insert(END, court20[2])
                        display_court20.config(bg='#00688B', fg="white")
                    else:
                        display_court20.delete(1.0, END)
                        display_court20.config(bg="#008B00")
                        display_court20.image_create(END, image=court_bg)
                
                elif list_of_months[int(month) - 1] == "July":
                    court1 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20)].get(1.0, END).split('\n')
                    court2 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 2].get(1.0, END).split('\n')
                    court3 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 3].get(1.0, END).split('\n')
                    court4 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 4].get(1.0, END).split('\n')
                    court5 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 5].get(1.0, END).split('\n')
                    court6 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 6].get(1.0, END).split('\n')
                    court7 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 7].get(1.0, END).split('\n')
                    court8 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 8].get(1.0, END).split('\n')
                    court9 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 9].get(1.0, END).split('\n')
                    court10 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 10].get(1.0, END).split('\n')
                    court11 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 11].get(1.0, END).split('\n')
                    court12 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 12].get(1.0, END).split('\n')
                    court13 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 13].get(1.0, END).split('\n')
                    court14 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 14].get(1.0, END).split('\n')
                    court15 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 15].get(1.0, END).split('\n')
                    court16 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 16].get(1.0, END).split('\n')
                    court17 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 17].get(1.0, END).split('\n')
                    court18 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 18].get(1.0, END).split('\n')
                    court19 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 19].get(1.0, END).split('\n')
                    court20 = jul_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 20].get(1.0, END).split('\n')

                    if court1 != ['','']:
                        display_court1.delete(1.0, END)
                        display_court1.insert(END, court1[0] + '\n')
                        display_court1.insert(END, court1[2])
                        display_court1.config(bg='#00688B', fg="white")
                    else:
                        display_court1.delete(1.0, END)
                        display_court1.config(bg="#008B00")
                        display_court1.image_create(END, image=court_bg)
                    if court2 != ['','']:
                        display_court2.delete(1.0, END)
                        display_court2.insert(END, court2[0] + '\n')
                        display_court2.insert(END, court2[2])
                        display_court2.config(bg='#00688B', fg="white")
                    else:
                        display_court2.delete(1.0, END)
                        display_court2.config(bg="#008B00")
                        display_court2.image_create(END, image=court_bg)
                    if court3 != ['','']:
                        display_court3.delete(1.0, END)
                        display_court3.insert(END, court3[0] + '\n')
                        display_court3.insert(END, court3[2])
                        display_court3.config(bg='#00688B', fg="white")
                    else:
                        display_court3.delete(1.0, END)
                        display_court3.config(bg="#008B00")
                        display_court3.image_create(END, image=court_bg)
                    if court4 != ['','']:
                        display_court4.delete(1.0, END)
                        display_court4.insert(END, court4[0] + '\n')
                        display_court4.insert(END, court4[2])
                        display_court4.config(bg='#00688B', fg="white")
                    else:
                        display_court4.delete(1.0, END)
                        display_court4.config(bg="#008B00")
                        display_court4.image_create(END, image=court_bg)
                    if court5 != ['','']:
                        display_court5.delete(1.0, END)
                        display_court5.insert(END, court5[0] + '\n')
                        display_court5.insert(END, court5[2])
                        display_court5.config(bg='#00688B', fg="white")
                    else:
                        display_court5.delete(1.0, END)
                        display_court5.config(bg="#008B00")
                        display_court5.image_create(END, image=court_bg)
                    if court6 != ['','']:
                        display_court6.delete(1.0, END)
                        display_court6.insert(END, court6[0] + '\n')
                        display_court6.insert(END, court6[2])
                        display_court6.config(bg='#00688B', fg="white")
                    else:
                        display_court6.delete(1.0, END)
                        display_court6.config(bg="#008B00")
                        display_court6.image_create(END, image=court_bg)
                    if court7 != ['','']:
                        display_court7.delete(1.0, END)
                        display_court7.insert(END, court7[0] + '\n')
                        display_court7.insert(END, court7[2])
                        display_court7.config(bg='#00688B', fg="white")
                    else:
                        display_court7.delete(1.0, END)
                        display_court7.config(bg="#008B00")
                        display_court7.image_create(END, image=court_bg)
                    if court8 != ['','']:
                        display_court8.delete(1.0, END)
                        display_court8.insert(END, court8[0] + '\n')
                        display_court8.insert(END, court8[2])
                        display_court8.config(bg='#00688B', fg="white")
                    else:
                        display_court8.delete(1.0, END)
                        display_court8.config(bg="#008B00")
                        display_court8.image_create(END, image=court_bg)
                    if court9 != ['','']:
                        display_court9.delete(1.0, END)
                        display_court9.insert(END, court9[0] + '\n')
                        display_court9.insert(END, court9[2])
                        display_court9.config(bg='#00688B', fg="white")
                    else:
                        display_court9.delete(1.0, END)
                        display_court9.config(bg="#008B00")
                        display_court9.image_create(END, image=court_bg)
                    if court10 != ['','']:
                        display_court10.delete(1.0, END)
                        display_court10.insert(END, court10[0] + '\n')
                        display_court10.insert(END, court10[2])
                        display_court10.config(bg='#00688B', fg="white")
                    else:
                        display_court10.delete(1.0, END)
                        display_court10.config(bg="#008B00")
                        display_court10.image_create(END, image=court_bg)
                    if court11 != ['','']:
                        display_court11.delete(1.0, END)
                        display_court11.insert(END, court11[0] + '\n')
                        display_court11.insert(END, court11[2])
                        display_court11.config(bg='#00688B', fg="white")
                    else:
                        display_court11.delete(1.0, END)
                        display_court11.config(bg="#008B00")
                        display_court11.image_create(END, image=court_bg)
                    if court12 != ['','']:
                        display_court12.delete(1.0, END)
                        display_court12.insert(END, court12[0] + '\n')
                        display_court12.insert(END, court12[2])
                        display_court12.config(bg='#00688B', fg="white")
                    else:
                        display_court12.delete(1.0, END)
                        display_court12.config(bg="#008B00")
                        display_court12.image_create(END, image=court_bg)
                    if court13 != ['','']:
                        display_court13.delete(1.0, END)
                        display_court13.insert(END, court13[0] + '\n')
                        display_court13.insert(END, court13[2])
                        display_court13.config(bg='#00688B', fg="white")
                    else:
                        display_court13.delete(1.0, END)
                        display_court13.config(bg="#008B00")
                        display_court13.image_create(END, image=court_bg)
                    if court14 != ['','']:
                        display_court14.delete(1.0, END)
                        display_court14.insert(END, court14[0] + '\n')
                        display_court14.insert(END, court14[2])
                        display_court14.config(bg='#00688B', fg="white")
                    else:
                        display_court14.delete(1.0, END)
                        display_court14.config(bg="#008B00")
                        display_court14.image_create(END, image=court_bg)
                    if court15 != ['','']:
                        display_court15.delete(1.0, END)
                        display_court15.insert(END, court15[0] + '\n')
                        display_court15.insert(END, court15[2])
                        display_court15.config(bg='#00688B', fg="white")
                    else:
                        display_court15.delete(1.0, END)
                        display_court15.config(bg="#008B00")
                        display_court15.image_create(END, image=court_bg)
                    if court16 != ['','']:
                        display_court16.delete(1.0, END)
                        display_court16.insert(END, court16[0] + '\n')
                        display_court16.insert(END, court16[2])
                        display_court16.config(bg='#00688B', fg="white")
                    else:
                        display_court16.delete(1.0, END)
                        display_court16.config(bg="#008B00")
                        display_court16.image_create(END, image=court_bg)
                    if court17 != ['','']:
                        display_court17.delete(1.0, END)
                        display_court17.insert(END, court17[0] + '\n')
                        display_court17.insert(END, court17[2])
                        display_court17.config(bg='#00688B', fg="white")
                    else:
                        display_court17.delete(1.0, END)
                        display_court17.config(bg="#008B00")
                        display_court17.image_create(END, image=court_bg)
                    if court18 != ['','']:
                        display_court18.delete(1.0, END)
                        display_court18.insert(END, court18[0] + '\n')
                        display_court18.insert(END, court18[2])
                        display_court18.config(bg='#00688B', fg="white")
                    else:
                        display_court18.delete(1.0, END)
                        display_court18.config(bg="008B00")
                        display_court18.image_create(END, image=court_bg)
                    if court19 != ['','']:
                        display_court19.delete(1.0, END)
                        display_court19.insert(END, court19[0] + '\n')
                        display_court19.insert(END, court19[2])
                        display_court19.config(bg='#00688B', fg="white")
                    else:
                        display_court19.delete(1.0, END)
                        display_court19.config(bg="#008B00")
                        display_court19.image_create(END, image=court_bg)
                    if court20 != ['','']:
                        display_court20.delete(1.0, END)
                        display_court20.insert(END, court20[0] + '\n')
                        display_court20.insert(END, court20[2])
                        display_court20.config(bg='#00688B', fg="white")
                    else:
                        display_court20.delete(1.0, END)
                        display_court20.config(bg="#008B00")
                        display_court20.image_create(END, image=court_bg)
                
                elif list_of_months[int(month) - 1] == "August":
                    court1 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20)].get(1.0, END).split('\n')
                    court2 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 2].get(1.0, END).split('\n')
                    court3 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 3].get(1.0, END).split('\n')
                    court4 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 4].get(1.0, END).split('\n')
                    court5 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 5].get(1.0, END).split('\n')
                    court6 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 6].get(1.0, END).split('\n')
                    court7 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 7].get(1.0, END).split('\n')
                    court8 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 8].get(1.0, END).split('\n')
                    court9 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 9].get(1.0, END).split('\n')
                    court10 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 10].get(1.0, END).split('\n')
                    court11 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 11].get(1.0, END).split('\n')
                    court12 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 12].get(1.0, END).split('\n')
                    court13 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 13].get(1.0, END).split('\n')
                    court14 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 14].get(1.0, END).split('\n')
                    court15 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 15].get(1.0, END).split('\n')
                    court16 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 16].get(1.0, END).split('\n')
                    court17 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 17].get(1.0, END).split('\n')
                    court18 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 18].get(1.0, END).split('\n')
                    court19 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 19].get(1.0, END).split('\n')
                    court20 = aug_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 20].get(1.0, END).split('\n')

                    if court1 != ['','']:
                        display_court1.delete(1.0, END)
                        display_court1.insert(END, court1[0] + '\n')
                        display_court1.insert(END, court1[2])
                        display_court1.config(bg='#00688B', fg="white")
                    else:
                        display_court1.delete(1.0, END)
                        display_court1.config(bg="#008B00")
                        display_court1.image_create(END, image=court_bg)
                    if court2 != ['','']:
                        display_court2.delete(1.0, END)
                        display_court2.insert(END, court2[0] + '\n')
                        display_court2.insert(END, court2[2])
                        display_court2.config(bg='#00688B', fg="white")
                    else:
                        display_court2.delete(1.0, END)
                        display_court2.config(bg="#008B00")
                        display_court2.image_create(END, image=court_bg)
                    if court3 != ['','']:
                        display_court3.delete(1.0, END)
                        display_court3.insert(END, court3[0] + '\n')
                        display_court3.insert(END, court3[2])
                        display_court3.config(bg='#00688B', fg="white")
                    else:
                        display_court3.delete(1.0, END)
                        display_court3.config(bg="#008B00")
                        display_court3.image_create(END, image=court_bg)
                    if court4 != ['','']:
                        display_court4.delete(1.0, END)
                        display_court4.insert(END, court4[0] + '\n')
                        display_court4.insert(END, court4[2])
                        display_court4.config(bg='#00688B', fg="white")
                    else:
                        display_court4.delete(1.0, END)
                        display_court4.config(bg="#008B00")
                        display_court4.image_create(END, image=court_bg)
                    if court5 != ['','']:
                        display_court5.delete(1.0, END)
                        display_court5.insert(END, court5[0] + '\n')
                        display_court5.insert(END, court5[2])
                        display_court5.config(bg='#00688B', fg="white")
                    else:
                        display_court5.delete(1.0, END)
                        display_court5.config(bg="#008B00")
                        display_court5.image_create(END, image=court_bg)
                    if court6 != ['','']:
                        display_court6.delete(1.0, END)
                        display_court6.insert(END, court6[0] + '\n')
                        display_court6.insert(END, court6[2])
                        display_court6.config(bg='#00688B', fg="white")
                    else:
                        display_court6.delete(1.0, END)
                        display_court6.config(bg="#008B00")
                        display_court6.image_create(END, image=court_bg)
                    if court7 != ['','']:
                        display_court7.delete(1.0, END)
                        display_court7.insert(END, court7[0] + '\n')
                        display_court7.insert(END, court7[2])
                        display_court7.config(bg='#00688B', fg="white")
                    else:
                        display_court7.delete(1.0, END)
                        display_court7.config(bg="#008B00")
                        display_court7.image_create(END, image=court_bg)
                    if court8 != ['','']:
                        display_court8.delete(1.0, END)
                        display_court8.insert(END, court8[0] + '\n')
                        display_court8.insert(END, court8[2])
                        display_court8.config(bg='#00688B', fg="white")
                    else:
                        display_court8.delete(1.0, END)
                        display_court8.config(bg="#008B00")
                        display_court8.image_create(END, image=court_bg)
                    if court9 != ['','']:
                        display_court9.delete(1.0, END)
                        display_court9.insert(END, court9[0] + '\n')
                        display_court9.insert(END, court9[2])
                        display_court9.config(bg='#00688B', fg="white")
                    else:
                        display_court9.delete(1.0, END)
                        display_court9.config(bg="#008B00")
                        display_court9.image_create(END, image=court_bg)
                    if court10 != ['','']:
                        display_court10.delete(1.0, END)
                        display_court10.insert(END, court10[0] + '\n')
                        display_court10.insert(END, court10[2])
                        display_court10.config(bg='#00688B', fg="white")
                    else:
                        display_court10.delete(1.0, END)
                        display_court10.config(bg="#008B00")
                        display_court10.image_create(END, image=court_bg)
                    if court11 != ['','']:
                        display_court11.delete(1.0, END)
                        display_court11.insert(END, court11[0] + '\n')
                        display_court11.insert(END, court11[2])
                        display_court11.config(bg='#00688B', fg="white")
                    else:
                        display_court11.delete(1.0, END)
                        display_court11.config(bg="#008B00")
                        display_court11.image_create(END, image=court_bg)
                    if court12 != ['','']:
                        display_court12.delete(1.0, END)
                        display_court12.insert(END, court12[0] + '\n')
                        display_court12.insert(END, court12[2])
                        display_court12.config(bg='#00688B', fg="white")
                    else:
                        display_court12.delete(1.0, END)
                        display_court12.config(bg="#008B00")
                        display_court12.image_create(END, image=court_bg)
                    if court13 != ['','']:
                        display_court13.delete(1.0, END)
                        display_court13.insert(END, court13[0] + '\n')
                        display_court13.insert(END, court13[2])
                        display_court13.config(bg='#00688B', fg="white")
                    else:
                        display_court13.delete(1.0, END)
                        display_court13.config(bg="#008B00")
                        display_court13.image_create(END, image=court_bg)
                    if court14 != ['','']:
                        display_court14.delete(1.0, END)
                        display_court14.insert(END, court14[0] + '\n')
                        display_court14.insert(END, court14[2])
                        display_court14.config(bg='#00688B', fg="white")
                    else:
                        display_court14.delete(1.0, END)
                        display_court14.config(bg="#008B00")
                        display_court14.image_create(END, image=court_bg)
                    if court15 != ['','']:
                        display_court15.delete(1.0, END)
                        display_court15.insert(END, court15[0] + '\n')
                        display_court15.insert(END, court15[2])
                        display_court15.config(bg='#00688B', fg="white")
                    else:
                        display_court15.delete(1.0, END)
                        display_court15.config(bg="#008B00")
                        display_court15.image_create(END, image=court_bg)
                    if court16 != ['','']:
                        display_court16.delete(1.0, END)
                        display_court16.insert(END, court16[0] + '\n')
                        display_court16.insert(END, court16[2])
                        display_court16.config(bg='#00688B', fg="white")
                    else:
                        display_court16.delete(1.0, END)
                        display_court16.config(bg="#008B00")
                        display_court16.image_create(END, image=court_bg)
                    if court17 != ['','']:
                        display_court17.delete(1.0, END)
                        display_court17.insert(END, court17[0] + '\n')
                        display_court17.insert(END, court17[2])
                        display_court17.config(bg='#00688B', fg="white")
                    else:
                        display_court17.delete(1.0, END)
                        display_court17.config(bg="#008B00")
                        display_court17.image_create(END, image=court_bg)
                    if court18 != ['','']:
                        display_court18.delete(1.0, END)
                        display_court18.insert(END, court18[0] + '\n')
                        display_court18.insert(END, court18[2])
                        display_court18.config(bg='#00688B', fg="white")
                    else:
                        display_court18.delete(1.0, END)
                        display_court18.config(bg="008B00")
                        display_court18.image_create(END, image=court_bg)
                    if court19 != ['','']:
                        display_court19.delete(1.0, END)
                        display_court19.insert(END, court19[0] + '\n')
                        display_court19.insert(END, court19[2])
                        display_court19.config(bg='#00688B', fg="white")
                    else:
                        display_court19.delete(1.0, END)
                        display_court19.config(bg="#008B00")
                        display_court19.image_create(END, image=court_bg)
                    if court20 != ['','']:
                        display_court20.delete(1.0, END)
                        display_court20.insert(END, court20[0] + '\n')
                        display_court20.insert(END, court20[2])
                        display_court20.config(bg='#00688B', fg="white")
                    else:
                        display_court20.delete(1.0, END)
                        display_court20.config(bg="#008B00")
                        display_court20.image_create(END, image=court_bg)

                elif list_of_months[int(month) - 1] == "September":
                    court1 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20)].get(1.0, END).split('\n')
                    court2 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 2].get(1.0, END).split('\n')
                    court3 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 3].get(1.0, END).split('\n')
                    court4 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 4].get(1.0, END).split('\n')
                    court5 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 5].get(1.0, END).split('\n')
                    court6 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 6].get(1.0, END).split('\n')
                    court7 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 7].get(1.0, END).split('\n')
                    court8 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 8].get(1.0, END).split('\n')
                    court9 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 9].get(1.0, END).split('\n')
                    court10 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 10].get(1.0, END).split('\n')
                    court11 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 11].get(1.0, END).split('\n')
                    court12 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 12].get(1.0, END).split('\n')
                    court13 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 13].get(1.0, END).split('\n')
                    court14 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 14].get(1.0, END).split('\n')
                    court15 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 15].get(1.0, END).split('\n')
                    court16 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 16].get(1.0, END).split('\n')
                    court17 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 17].get(1.0, END).split('\n')
                    court18 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 18].get(1.0, END).split('\n')
                    court19 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 19].get(1.0, END).split('\n')
                    court20 = sep_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 20].get(1.0, END).split('\n')

                    if court1 != ['','']:
                        display_court1.delete(1.0, END)
                        display_court1.insert(END, court1[0] + '\n')
                        display_court1.insert(END, court1[2])
                        display_court1.config(bg='#00688B', fg="white")
                    else:
                        display_court1.delete(1.0, END)
                        display_court1.config(bg="#008B00")
                        display_court1.image_create(END, image=court_bg)
                    if court2 != ['','']:
                        display_court2.delete(1.0, END)
                        display_court2.insert(END, court2[0] + '\n')
                        display_court2.insert(END, court2[2])
                        display_court2.config(bg='#00688B', fg="white")
                    else:
                        display_court2.delete(1.0, END)
                        display_court2.config(bg="#008B00")
                        display_court2.image_create(END, image=court_bg)
                    if court3 != ['','']:
                        display_court3.delete(1.0, END)
                        display_court3.insert(END, court3[0] + '\n')
                        display_court3.insert(END, court3[2])
                        display_court3.config(bg='#00688B', fg="white")
                    else:
                        display_court3.delete(1.0, END)
                        display_court3.config(bg="#008B00")
                        display_court3.image_create(END, image=court_bg)
                    if court4 != ['','']:
                        display_court4.delete(1.0, END)
                        display_court4.insert(END, court4[0] + '\n')
                        display_court4.insert(END, court4[2])
                        display_court4.config(bg='#00688B', fg="white")
                    else:
                        display_court4.delete(1.0, END)
                        display_court4.config(bg="#008B00")
                        display_court4.image_create(END, image=court_bg)
                    if court5 != ['','']:
                        display_court5.delete(1.0, END)
                        display_court5.insert(END, court5[0] + '\n')
                        display_court5.insert(END, court5[2])
                        display_court5.config(bg='#00688B', fg="white")
                    else:
                        display_court5.delete(1.0, END)
                        display_court5.config(bg="#008B00")
                        display_court5.image_create(END, image=court_bg)
                    if court6 != ['','']:
                        display_court6.delete(1.0, END)
                        display_court6.insert(END, court6[0] + '\n')
                        display_court6.insert(END, court6[2])
                        display_court6.config(bg='#00688B', fg="white")
                    else:
                        display_court6.delete(1.0, END)
                        display_court6.config(bg="#008B00")
                        display_court6.image_create(END, image=court_bg)
                    if court7 != ['','']:
                        display_court7.delete(1.0, END)
                        display_court7.insert(END, court7[0] + '\n')
                        display_court7.insert(END, court7[2])
                        display_court7.config(bg='#00688B', fg="white")
                    else:
                        display_court7.delete(1.0, END)
                        display_court7.config(bg="#008B00")
                        display_court7.image_create(END, image=court_bg)
                    if court8 != ['','']:
                        display_court8.delete(1.0, END)
                        display_court8.insert(END, court8[0] + '\n')
                        display_court8.insert(END, court8[2])
                        display_court8.config(bg='#00688B', fg="white")
                    else:
                        display_court8.delete(1.0, END)
                        display_court8.config(bg="#008B00")
                        display_court8.image_create(END, image=court_bg)
                    if court9 != ['','']:
                        display_court9.delete(1.0, END)
                        display_court9.insert(END, court9[0] + '\n')
                        display_court9.insert(END, court9[2])
                        display_court9.config(bg='#00688B', fg="white")
                    else:
                        display_court9.delete(1.0, END)
                        display_court9.config(bg="#008B00")
                        display_court9.image_create(END, image=court_bg)
                    if court10 != ['','']:
                        display_court10.delete(1.0, END)
                        display_court10.insert(END, court10[0] + '\n')
                        display_court10.insert(END, court10[2])
                        display_court10.config(bg='#00688B', fg="white")
                    else:
                        display_court10.delete(1.0, END)
                        display_court10.config(bg="#008B00")
                        display_court10.image_create(END, image=court_bg)
                    if court11 != ['','']:
                        display_court11.delete(1.0, END)
                        display_court11.insert(END, court11[0] + '\n')
                        display_court11.insert(END, court11[2])
                        display_court11.config(bg='#00688B', fg="white")
                    else:
                        display_court11.delete(1.0, END)
                        display_court11.config(bg="#008B00")
                        display_court11.image_create(END, image=court_bg)
                    if court12 != ['','']:
                        display_court12.delete(1.0, END)
                        display_court12.insert(END, court12[0] + '\n')
                        display_court12.insert(END, court12[2])
                        display_court12.config(bg='#00688B', fg="white")
                    else:
                        display_court12.delete(1.0, END)
                        display_court12.config(bg="#008B00")
                        display_court12.image_create(END, image=court_bg)
                    if court13 != ['','']:
                        display_court13.delete(1.0, END)
                        display_court13.insert(END, court13[0] + '\n')
                        display_court13.insert(END, court13[2])
                        display_court13.config(bg='#00688B', fg="white")
                    else:
                        display_court13.delete(1.0, END)
                        display_court13.config(bg="#008B00")
                        display_court13.image_create(END, image=court_bg)
                    if court14 != ['','']:
                        display_court14.delete(1.0, END)
                        display_court14.insert(END, court14[0] + '\n')
                        display_court14.insert(END, court14[2])
                        display_court14.config(bg='#00688B', fg="white")
                    else:
                        display_court14.delete(1.0, END)
                        display_court14.config(bg="#008B00")
                        display_court14.image_create(END, image=court_bg)
                    if court15 != ['','']:
                        display_court15.delete(1.0, END)
                        display_court15.insert(END, court15[0] + '\n')
                        display_court15.insert(END, court15[2])
                        display_court15.config(bg='#00688B', fg="white")
                    else:
                        display_court15.delete(1.0, END)
                        display_court15.config(bg="#008B00")
                        display_court15.image_create(END, image=court_bg)
                    if court16 != ['','']:
                        display_court16.delete(1.0, END)
                        display_court16.insert(END, court16[0] + '\n')
                        display_court16.insert(END, court16[2])
                        display_court16.config(bg='#00688B', fg="white")
                    else:
                        display_court16.delete(1.0, END)
                        display_court16.config(bg="#008B00")
                        display_court16.image_create(END, image=court_bg)
                    if court17 != ['','']:
                        display_court17.delete(1.0, END)
                        display_court17.insert(END, court17[0] + '\n')
                        display_court17.insert(END, court17[2])
                        display_court17.config(bg='#00688B', fg="white")
                    else:
                        display_court17.delete(1.0, END)
                        display_court17.config(bg="#008B00")
                        display_court17.image_create(END, image=court_bg)
                    if court18 != ['','']:
                        display_court18.delete(1.0, END)
                        display_court18.insert(END, court18[0] + '\n')
                        display_court18.insert(END, court18[2])
                        display_court18.config(bg='#00688B', fg="white")
                    else:
                        display_court18.delete(1.0, END)
                        display_court18.config(bg="008B00")
                        display_court18.image_create(END, image=court_bg)
                    if court19 != ['','']:
                        display_court19.delete(1.0, END)
                        display_court19.insert(END, court19[0] + '\n')
                        display_court19.insert(END, court19[2])
                        display_court19.config(bg='#00688B', fg="white")
                    else:
                        display_court19.delete(1.0, END)
                        display_court19.config(bg="#008B00")
                        display_court19.image_create(END, image=court_bg)
                    if court20 != ['','']:
                        display_court20.delete(1.0, END)
                        display_court20.insert(END, court20[0] + '\n')
                        display_court20.insert(END, court20[2])
                        display_court20.config(bg='#00688B', fg="white")
                    else:
                        display_court20.delete(1.0, END)
                        display_court20.config(bg="#008B00")
                        display_court20.image_create(END, image=court_bg)
                
                elif list_of_months[int(month) - 1] == "October":
                    court1 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20)].get(1.0, END).split('\n')
                    court2 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 2].get(1.0, END).split('\n')
                    court3 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 3].get(1.0, END).split('\n')
                    court4 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 4].get(1.0, END).split('\n')
                    court5 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 5].get(1.0, END).split('\n')
                    court6 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 6].get(1.0, END).split('\n')
                    court7 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 7].get(1.0, END).split('\n')
                    court8 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 8].get(1.0, END).split('\n')
                    court9 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 9].get(1.0, END).split('\n')
                    court10 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 10].get(1.0, END).split('\n')
                    court11 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 11].get(1.0, END).split('\n')
                    court12 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 12].get(1.0, END).split('\n')
                    court13 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 13].get(1.0, END).split('\n')
                    court14 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 14].get(1.0, END).split('\n')
                    court15 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 15].get(1.0, END).split('\n')
                    court16 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 16].get(1.0, END).split('\n')
                    court17 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 17].get(1.0, END).split('\n')
                    court18 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 18].get(1.0, END).split('\n')
                    court19 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 19].get(1.0, END).split('\n')
                    court20 = oct_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 20].get(1.0, END).split('\n')

                    if court1 != ['','']:
                        display_court1.delete(1.0, END)
                        display_court1.insert(END, court1[0] + '\n')
                        display_court1.insert(END, court1[2])
                        display_court1.config(bg='#00688B', fg="white")
                    else:
                        display_court1.delete(1.0, END)
                        display_court1.config(bg="#008B00")
                        display_court1.image_create(END, image=court_bg)
                    if court2 != ['','']:
                        display_court2.delete(1.0, END)
                        display_court2.insert(END, court2[0] + '\n')
                        display_court2.insert(END, court2[2])
                        display_court2.config(bg='#00688B', fg="white")
                    else:
                        display_court2.delete(1.0, END)
                        display_court2.config(bg="#008B00")
                        display_court2.image_create(END, image=court_bg)
                    if court3 != ['','']:
                        display_court3.delete(1.0, END)
                        display_court3.insert(END, court3[0] + '\n')
                        display_court3.insert(END, court3[2])
                        display_court3.config(bg='#00688B', fg="white")
                    else:
                        display_court3.delete(1.0, END)
                        display_court3.config(bg="#008B00")
                        display_court3.image_create(END, image=court_bg)
                    if court4 != ['','']:
                        display_court4.delete(1.0, END)
                        display_court4.insert(END, court4[0] + '\n')
                        display_court4.insert(END, court4[2])
                        display_court4.config(bg='#00688B', fg="white")
                    else:
                        display_court4.delete(1.0, END)
                        display_court4.config(bg="#008B00")
                        display_court4.image_create(END, image=court_bg)
                    if court5 != ['','']:
                        display_court5.delete(1.0, END)
                        display_court5.insert(END, court5[0] + '\n')
                        display_court5.insert(END, court5[2])
                        display_court5.config(bg='#00688B', fg="white")
                    else:
                        display_court5.delete(1.0, END)
                        display_court5.config(bg="#008B00")
                        display_court5.image_create(END, image=court_bg)
                    if court6 != ['','']:
                        display_court6.delete(1.0, END)
                        display_court6.insert(END, court6[0] + '\n')
                        display_court6.insert(END, court6[2])
                        display_court6.config(bg='#00688B', fg="white")
                    else:
                        display_court6.delete(1.0, END)
                        display_court6.config(bg="#008B00")
                        display_court6.image_create(END, image=court_bg)
                    if court7 != ['','']:
                        display_court7.delete(1.0, END)
                        display_court7.insert(END, court7[0] + '\n')
                        display_court7.insert(END, court7[2])
                        display_court7.config(bg='#00688B', fg="white")
                    else:
                        display_court7.delete(1.0, END)
                        display_court7.config(bg="#008B00")
                        display_court7.image_create(END, image=court_bg)
                    if court8 != ['','']:
                        display_court8.delete(1.0, END)
                        display_court8.insert(END, court8[0] + '\n')
                        display_court8.insert(END, court8[2])
                        display_court8.config(bg='#00688B', fg="white")
                    else:
                        display_court8.delete(1.0, END)
                        display_court8.config(bg="#008B00")
                        display_court8.image_create(END, image=court_bg)
                    if court9 != ['','']:
                        display_court9.delete(1.0, END)
                        display_court9.insert(END, court9[0] + '\n')
                        display_court9.insert(END, court9[2])
                        display_court9.config(bg='#00688B', fg="white")
                    else:
                        display_court9.delete(1.0, END)
                        display_court9.config(bg="#008B00")
                        display_court9.image_create(END, image=court_bg)
                    if court10 != ['','']:
                        display_court10.delete(1.0, END)
                        display_court10.insert(END, court10[0] + '\n')
                        display_court10.insert(END, court10[2])
                        display_court10.config(bg='#00688B', fg="white")
                    else:
                        display_court10.delete(1.0, END)
                        display_court10.config(bg="#008B00")
                        display_court10.image_create(END, image=court_bg)
                    if court11 != ['','']:
                        display_court11.delete(1.0, END)
                        display_court11.insert(END, court11[0] + '\n')
                        display_court11.insert(END, court11[2])
                        display_court11.config(bg='#00688B', fg="white")
                    else:
                        display_court11.delete(1.0, END)
                        display_court11.config(bg="#008B00")
                        display_court11.image_create(END, image=court_bg)
                    if court12 != ['','']:
                        display_court12.delete(1.0, END)
                        display_court12.insert(END, court12[0] + '\n')
                        display_court12.insert(END, court12[2])
                        display_court12.config(bg='#00688B', fg="white")
                    else:
                        display_court12.delete(1.0, END)
                        display_court12.config(bg="#008B00")
                        display_court12.image_create(END, image=court_bg)
                    if court13 != ['','']:
                        display_court13.delete(1.0, END)
                        display_court13.insert(END, court13[0] + '\n')
                        display_court13.insert(END, court13[2])
                        display_court13.config(bg='#00688B', fg="white")
                    else:
                        display_court13.delete(1.0, END)
                        display_court13.config(bg="#008B00")
                        display_court13.image_create(END, image=court_bg)
                    if court14 != ['','']:
                        display_court14.delete(1.0, END)
                        display_court14.insert(END, court14[0] + '\n')
                        display_court14.insert(END, court14[2])
                        display_court14.config(bg='#00688B', fg="white")
                    else:
                        display_court14.delete(1.0, END)
                        display_court14.config(bg="#008B00")
                        display_court14.image_create(END, image=court_bg)
                    if court15 != ['','']:
                        display_court15.delete(1.0, END)
                        display_court15.insert(END, court15[0] + '\n')
                        display_court15.insert(END, court15[2])
                        display_court15.config(bg='#00688B', fg="white")
                    else:
                        display_court15.delete(1.0, END)
                        display_court15.config(bg="#008B00")
                        display_court15.image_create(END, image=court_bg)
                    if court16 != ['','']:
                        display_court16.delete(1.0, END)
                        display_court16.insert(END, court16[0] + '\n')
                        display_court16.insert(END, court16[2])
                        display_court16.config(bg='#00688B', fg="white")
                    else:
                        display_court16.delete(1.0, END)
                        display_court16.config(bg="#008B00")
                        display_court16.image_create(END, image=court_bg)
                    if court17 != ['','']:
                        display_court17.delete(1.0, END)
                        display_court17.insert(END, court17[0] + '\n')
                        display_court17.insert(END, court17[2])
                        display_court17.config(bg='#00688B', fg="white")
                    else:
                        display_court17.delete(1.0, END)
                        display_court17.config(bg="#008B00")
                        display_court17.image_create(END, image=court_bg)
                    if court18 != ['','']:
                        display_court18.delete(1.0, END)
                        display_court18.insert(END, court18[0] + '\n')
                        display_court18.insert(END, court18[2])
                        display_court18.config(bg='#00688B', fg="white")
                    else:
                        display_court18.delete(1.0, END)
                        display_court18.config(bg="008B00")
                        display_court18.image_create(END, image=court_bg)
                    if court19 != ['','']:
                        display_court19.delete(1.0, END)
                        display_court19.insert(END, court19[0] + '\n')
                        display_court19.insert(END, court19[2])
                        display_court19.config(bg='#00688B', fg="white")
                    else:
                        display_court19.delete(1.0, END)
                        display_court19.config(bg="#008B00")
                        display_court19.image_create(END, image=court_bg)
                    if court20 != ['','']:
                        display_court20.delete(1.0, END)
                        display_court20.insert(END, court20[0] + '\n')
                        display_court20.insert(END, court20[2])
                        display_court20.config(bg='#00688B', fg="white")
                    else:
                        display_court20.delete(1.0, END)
                        display_court20.config(bg="#008B00")
                        display_court20.image_create(END, image=court_bg)

                elif list_of_months[int(month) - 1] == "November":
                    court1 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20)].get(1.0, END).split('\n')
                    court2 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 2].get(1.0, END).split('\n')
                    court3 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 3].get(1.0, END).split('\n')
                    court4 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 4].get(1.0, END).split('\n')
                    court5 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 5].get(1.0, END).split('\n')
                    court6 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 6].get(1.0, END).split('\n')
                    court7 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 7].get(1.0, END).split('\n')
                    court8 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 8].get(1.0, END).split('\n')
                    court9 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 9].get(1.0, END).split('\n')
                    court10 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 10].get(1.0, END).split('\n')
                    court11 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 11].get(1.0, END).split('\n')
                    court12 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 12].get(1.0, END).split('\n')
                    court13 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 13].get(1.0, END).split('\n')
                    court14 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 14].get(1.0, END).split('\n')
                    court15 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 15].get(1.0, END).split('\n')
                    court16 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 16].get(1.0, END).split('\n')
                    court17 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 17].get(1.0, END).split('\n')
                    court18 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 18].get(1.0, END).split('\n')
                    court19 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 19].get(1.0, END).split('\n')
                    court20 = nov_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 20].get(1.0, END).split('\n')

                    if court1 != ['','']:
                        display_court1.delete(1.0, END)
                        display_court1.insert(END, court1[0] + '\n')
                        display_court1.insert(END, court1[2])
                        display_court1.config(bg='#00688B', fg="white")
                    else:
                        display_court1.delete(1.0, END)
                        display_court1.config(bg="#008B00")
                        display_court1.image_create(END, image=court_bg)
                    if court2 != ['','']:
                        display_court2.delete(1.0, END)
                        display_court2.insert(END, court2[0] + '\n')
                        display_court2.insert(END, court2[2])
                        display_court2.config(bg='#00688B', fg="white")
                    else:
                        display_court2.delete(1.0, END)
                        display_court2.config(bg="#008B00")
                        display_court2.image_create(END, image=court_bg)
                    if court3 != ['','']:
                        display_court3.delete(1.0, END)
                        display_court3.insert(END, court3[0] + '\n')
                        display_court3.insert(END, court3[2])
                        display_court3.config(bg='#00688B', fg="white")
                    else:
                        display_court3.delete(1.0, END)
                        display_court3.config(bg="#008B00")
                        display_court3.image_create(END, image=court_bg)
                    if court4 != ['','']:
                        display_court4.delete(1.0, END)
                        display_court4.insert(END, court4[0] + '\n')
                        display_court4.insert(END, court4[2])
                        display_court4.config(bg='#00688B', fg="white")
                    else:
                        display_court4.delete(1.0, END)
                        display_court4.config(bg="#008B00")
                        display_court4.image_create(END, image=court_bg)
                    if court5 != ['','']:
                        display_court5.delete(1.0, END)
                        display_court5.insert(END, court5[0] + '\n')
                        display_court5.insert(END, court5[2])
                        display_court5.config(bg='#00688B', fg="white")
                    else:
                        display_court5.delete(1.0, END)
                        display_court5.config(bg="#008B00")
                        display_court5.image_create(END, image=court_bg)
                    if court6 != ['','']:
                        display_court6.delete(1.0, END)
                        display_court6.insert(END, court6[0] + '\n')
                        display_court6.insert(END, court6[2])
                        display_court6.config(bg='#00688B', fg="white")
                    else:
                        display_court6.delete(1.0, END)
                        display_court6.config(bg="#008B00")
                        display_court6.image_create(END, image=court_bg)
                    if court7 != ['','']:
                        display_court7.delete(1.0, END)
                        display_court7.insert(END, court7[0] + '\n')
                        display_court7.insert(END, court7[2])
                        display_court7.config(bg='#00688B', fg="white")
                    else:
                        display_court7.delete(1.0, END)
                        display_court7.config(bg="#008B00")
                        display_court7.image_create(END, image=court_bg)
                    if court8 != ['','']:
                        display_court8.delete(1.0, END)
                        display_court8.insert(END, court8[0] + '\n')
                        display_court8.insert(END, court8[2])
                        display_court8.config(bg='#00688B', fg="white")
                    else:
                        display_court8.delete(1.0, END)
                        display_court8.config(bg="#008B00")
                        display_court8.image_create(END, image=court_bg)
                    if court9 != ['','']:
                        display_court9.delete(1.0, END)
                        display_court9.insert(END, court9[0] + '\n')
                        display_court9.insert(END, court9[2])
                        display_court9.config(bg='#00688B', fg="white")
                    else:
                        display_court9.delete(1.0, END)
                        display_court9.config(bg="#008B00")
                        display_court9.image_create(END, image=court_bg)
                    if court10 != ['','']:
                        display_court10.delete(1.0, END)
                        display_court10.insert(END, court10[0] + '\n')
                        display_court10.insert(END, court10[2])
                        display_court10.config(bg='#00688B', fg="white")
                    else:
                        display_court10.delete(1.0, END)
                        display_court10.config(bg="#008B00")
                        display_court10.image_create(END, image=court_bg)
                    if court11 != ['','']:
                        display_court11.delete(1.0, END)
                        display_court11.insert(END, court11[0] + '\n')
                        display_court11.insert(END, court11[2])
                        display_court11.config(bg='#00688B', fg="white")
                    else:
                        display_court11.delete(1.0, END)
                        display_court11.config(bg="#008B00")
                        display_court11.image_create(END, image=court_bg)
                    if court12 != ['','']:
                        display_court12.delete(1.0, END)
                        display_court12.insert(END, court12[0] + '\n')
                        display_court12.insert(END, court12[2])
                        display_court12.config(bg='#00688B', fg="white")
                    else:
                        display_court12.delete(1.0, END)
                        display_court12.config(bg="#008B00")
                        display_court12.image_create(END, image=court_bg)
                    if court13 != ['','']:
                        display_court13.delete(1.0, END)
                        display_court13.insert(END, court13[0] + '\n')
                        display_court13.insert(END, court13[2])
                        display_court13.config(bg='#00688B', fg="white")
                    else:
                        display_court13.delete(1.0, END)
                        display_court13.config(bg="#008B00")
                        display_court13.image_create(END, image=court_bg)
                    if court14 != ['','']:
                        display_court14.delete(1.0, END)
                        display_court14.insert(END, court14[0] + '\n')
                        display_court14.insert(END, court14[2])
                        display_court14.config(bg='#00688B', fg="white")
                    else:
                        display_court14.delete(1.0, END)
                        display_court14.config(bg="#008B00")
                        display_court14.image_create(END, image=court_bg)
                    if court15 != ['','']:
                        display_court15.delete(1.0, END)
                        display_court15.insert(END, court15[0] + '\n')
                        display_court15.insert(END, court15[2])
                        display_court15.config(bg='#00688B', fg="white")
                    else:
                        display_court15.delete(1.0, END)
                        display_court15.config(bg="#008B00")
                        display_court15.image_create(END, image=court_bg)
                    if court16 != ['','']:
                        display_court16.delete(1.0, END)
                        display_court16.insert(END, court16[0] + '\n')
                        display_court16.insert(END, court16[2])
                        display_court16.config(bg='#00688B', fg="white")
                    else:
                        display_court16.delete(1.0, END)
                        display_court16.config(bg="#008B00")
                        display_court16.image_create(END, image=court_bg)
                    if court17 != ['','']:
                        display_court17.delete(1.0, END)
                        display_court17.insert(END, court17[0] + '\n')
                        display_court17.insert(END, court17[2])
                        display_court17.config(bg='#00688B', fg="white")
                    else:
                        display_court17.delete(1.0, END)
                        display_court17.config(bg="#008B00")
                        display_court17.image_create(END, image=court_bg)
                    if court18 != ['','']:
                        display_court18.delete(1.0, END)
                        display_court18.insert(END, court18[0] + '\n')
                        display_court18.insert(END, court18[2])
                        display_court18.config(bg='#00688B', fg="white")
                    else:
                        display_court18.delete(1.0, END)
                        display_court18.config(bg="008B00")
                        display_court18.image_create(END, image=court_bg)
                    if court19 != ['','']:
                        display_court19.delete(1.0, END)
                        display_court19.insert(END, court19[0] + '\n')
                        display_court19.insert(END, court19[2])
                        display_court19.config(bg='#00688B', fg="white")
                    else:
                        display_court19.delete(1.0, END)
                        display_court19.config(bg="#008B00")
                        display_court19.image_create(END, image=court_bg)
                    if court20 != ['','']:
                        display_court20.delete(1.0, END)
                        display_court20.insert(END, court20[0] + '\n')
                        display_court20.insert(END, court20[2])
                        display_court20.config(bg='#00688B', fg="white")
                    else:
                        display_court20.delete(1.0, END)
                        display_court20.config(bg="#008B00")
                        display_court20.image_create(END, image=court_bg)

                elif list_of_months[int(month) - 1] == "December":
                    court1 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20)].get(1.0, END).split('\n')
                    court2 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 2].get(1.0, END).split('\n')
                    court3 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 3].get(1.0, END).split('\n')
                    court4 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 4].get(1.0, END).split('\n')
                    court5 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 5].get(1.0, END).split('\n')
                    court6 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 6].get(1.0, END).split('\n')
                    court7 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 7].get(1.0, END).split('\n')
                    court8 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 8].get(1.0, END).split('\n')
                    court9 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 9].get(1.0, END).split('\n')
                    court10 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 10].get(1.0, END).split('\n')
                    court11 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 11].get(1.0, END).split('\n')
                    court12 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 12].get(1.0, END).split('\n')
                    court13 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 13].get(1.0, END).split('\n')
                    court14 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 14].get(1.0, END).split('\n')
                    court15 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 15].get(1.0, END).split('\n')
                    court16 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 16].get(1.0, END).split('\n')
                    court17 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 17].get(1.0, END).split('\n')
                    court18 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 18].get(1.0, END).split('\n')
                    court19 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 19].get(1.0, END).split('\n')
                    court20 = dec_courtlist[((((int(day)-1)*24) + int(hour)) * 20) + 20].get(1.0, END).split('\n')

                    if court1 != ['','']:
                        display_court1.delete(1.0, END)
                        display_court1.insert(END, court1[0] + '\n')
                        display_court1.insert(END, court1[2])
                        display_court1.config(bg='#00688B', fg="white")
                    else:
                        display_court1.delete(1.0, END)
                        display_court1.config(bg="#008B00")
                        display_court1.image_create(END, image=court_bg)
                    if court2 != ['','']:
                        display_court2.delete(1.0, END)
                        display_court2.insert(END, court2[0] + '\n')
                        display_court2.insert(END, court2[2])
                        display_court2.config(bg='#00688B', fg="white")
                    else:
                        display_court2.delete(1.0, END)
                        display_court2.config(bg="#008B00")
                        display_court2.image_create(END, image=court_bg)
                    if court3 != ['','']:
                        display_court3.delete(1.0, END)
                        display_court3.insert(END, court3[0] + '\n')
                        display_court3.insert(END, court3[2])
                        display_court3.config(bg='#00688B', fg="white")
                    else:
                        display_court3.delete(1.0, END)
                        display_court3.config(bg="#008B00")
                        display_court3.image_create(END, image=court_bg)
                    if court4 != ['','']:
                        display_court4.delete(1.0, END)
                        display_court4.insert(END, court4[0] + '\n')
                        display_court4.insert(END, court4[2])
                        display_court4.config(bg='#00688B', fg="white")
                    else:
                        display_court4.delete(1.0, END)
                        display_court4.config(bg="#008B00")
                        display_court4.image_create(END, image=court_bg)
                    if court5 != ['','']:
                        display_court5.delete(1.0, END)
                        display_court5.insert(END, court5[0] + '\n')
                        display_court5.insert(END, court5[2])
                        display_court5.config(bg='#00688B', fg="white")
                    else:
                        display_court5.delete(1.0, END)
                        display_court5.config(bg="#008B00")
                        display_court5.image_create(END, image=court_bg)
                    if court6 != ['','']:
                        display_court6.delete(1.0, END)
                        display_court6.insert(END, court6[0] + '\n')
                        display_court6.insert(END, court6[2])
                        display_court6.config(bg='#00688B', fg="white")
                    else:
                        display_court6.delete(1.0, END)
                        display_court6.config(bg="#008B00")
                        display_court6.image_create(END, image=court_bg)
                    if court7 != ['','']:
                        display_court7.delete(1.0, END)
                        display_court7.insert(END, court7[0] + '\n')
                        display_court7.insert(END, court7[2])
                        display_court7.config(bg='#00688B', fg="white")
                    else:
                        display_court7.delete(1.0, END)
                        display_court7.config(bg="#008B00")
                        display_court7.image_create(END, image=court_bg)
                    if court8 != ['','']:
                        display_court8.delete(1.0, END)
                        display_court8.insert(END, court8[0] + '\n')
                        display_court8.insert(END, court8[2])
                        display_court8.config(bg='#00688B', fg="white")
                    else:
                        display_court8.delete(1.0, END)
                        display_court8.config(bg="#008B00")
                        display_court8.image_create(END, image=court_bg)
                    if court9 != ['','']:
                        display_court9.delete(1.0, END)
                        display_court9.insert(END, court9[0] + '\n')
                        display_court9.insert(END, court9[2])
                        display_court9.config(bg='#00688B', fg="white")
                    else:
                        display_court9.delete(1.0, END)
                        display_court9.config(bg="#008B00")
                        display_court9.image_create(END, image=court_bg)
                    if court10 != ['','']:
                        display_court10.delete(1.0, END)
                        display_court10.insert(END, court10[0] + '\n')
                        display_court10.insert(END, court10[2])
                        display_court10.config(bg='#00688B', fg="white")
                    else:
                        display_court10.delete(1.0, END)
                        display_court10.config(bg="#008B00")
                        display_court10.image_create(END, image=court_bg)
                    if court11 != ['','']:
                        display_court11.delete(1.0, END)
                        display_court11.insert(END, court11[0] + '\n')
                        display_court11.insert(END, court11[2])
                        display_court11.config(bg='#00688B', fg="white")
                    else:
                        display_court11.delete(1.0, END)
                        display_court11.config(bg="#008B00")
                        display_court11.image_create(END, image=court_bg)
                    if court12 != ['','']:
                        display_court12.delete(1.0, END)
                        display_court12.insert(END, court12[0] + '\n')
                        display_court12.insert(END, court12[2])
                        display_court12.config(bg='#00688B', fg="white")
                    else:
                        display_court12.delete(1.0, END)
                        display_court12.config(bg="#008B00")
                        display_court12.image_create(END, image=court_bg)
                    if court13 != ['','']:
                        display_court13.delete(1.0, END)
                        display_court13.insert(END, court13[0] + '\n')
                        display_court13.insert(END, court13[2])
                        display_court13.config(bg='#00688B', fg="white")
                    else:
                        display_court13.delete(1.0, END)
                        display_court13.config(bg="#008B00")
                        display_court13.image_create(END, image=court_bg)
                    if court14 != ['','']:
                        display_court14.delete(1.0, END)
                        display_court14.insert(END, court14[0] + '\n')
                        display_court14.insert(END, court14[2])
                        display_court14.config(bg='#00688B', fg="white")
                    else:
                        display_court14.delete(1.0, END)
                        display_court14.config(bg="#008B00")
                        display_court14.image_create(END, image=court_bg)
                    if court15 != ['','']:
                        display_court15.delete(1.0, END)
                        display_court15.insert(END, court15[0] + '\n')
                        display_court15.insert(END, court15[2])
                        display_court15.config(bg='#00688B', fg="white")
                    else:
                        display_court15.delete(1.0, END)
                        display_court15.config(bg="#008B00")
                        display_court15.image_create(END, image=court_bg)
                    if court16 != ['','']:
                        display_court16.delete(1.0, END)
                        display_court16.insert(END, court16[0] + '\n')
                        display_court16.insert(END, court16[2])
                        display_court16.config(bg='#00688B', fg="white")
                    else:
                        display_court16.delete(1.0, END)
                        display_court16.config(bg="#008B00")
                        display_court16.image_create(END, image=court_bg)
                    if court17 != ['','']:
                        display_court17.delete(1.0, END)
                        display_court17.insert(END, court17[0] + '\n')
                        display_court17.insert(END, court17[2])
                        display_court17.config(bg='#00688B', fg="white")
                    else:
                        display_court17.delete(1.0, END)
                        display_court17.config(bg="#008B00")
                        display_court17.image_create(END, image=court_bg)
                    if court18 != ['','']:
                        display_court18.delete(1.0, END)
                        display_court18.insert(END, court18[0] + '\n')
                        display_court18.insert(END, court18[2])
                        display_court18.config(bg='#00688B', fg="white")
                    else:
                        display_court18.delete(1.0, END)
                        display_court18.config(bg="008B00")
                        display_court18.image_create(END, image=court_bg)
                    if court19 != ['','']:
                        display_court19.delete(1.0, END)
                        display_court19.insert(END, court19[0] + '\n')
                        display_court19.insert(END, court19[2])
                        display_court19.config(bg='#00688B', fg="white")
                    else:
                        display_court19.delete(1.0, END)
                        display_court19.config(bg="#008B00")
                        display_court19.image_create(END, image=court_bg)
                    if court20 != ['','']:
                        display_court20.delete(1.0, END)
                        display_court20.insert(END, court20[0] + '\n')
                        display_court20.insert(END, court20[2])
                        display_court20.config(bg='#00688B', fg="white")
                    else:
                        display_court20.delete(1.0, END)
                        display_court20.config(bg="#008B00")
                        display_court20.image_create(END, image=court_bg)
                
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
    
    

def start_up(): #The start-up function automatically re-inserts

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    '''Window Settings'''
    startup_window = Toplevel()
    startup_window.title("Court Loading")
    startup_window.geometry("400x400")
    startup_window.configure(bg='lightblue')

    '''Logo Image'''
    img = Image.open(INSERT COMPANY LOGO IMAGE HERE)
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

        with open('bookingDataStorage.txt', 'r') as f:    
            for line in f:
                line_list.append(line.strip('\n'))

        f.close()

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
                
                    if (month == "January") and ("January" in date):
                        if "January" not in activated_list:
                            january_courts()
                            startup_insertion(name, num, code, month, time_info)
                            activated_list.append("January")
                        else:
                            startup_insertion(name, num, code, month, time_info) 
                    elif (month == "February") and ("February" in date):
                        if "February" not in activated_list:
                            february_courts()
                            startup_insertion(name, num, code, month, time_info)
                            activated_list.append("February")
                        else:
                            startup_insertion(name, num, code, month, time_info)
                    elif (month == "March") and ("March" in date):
                        if "March" not in activated_list:
                            march_courts()
                            startup_insertion(name, num, code, month, time_info)
                            activated_list.append("March")
                        else:
                            startup_insertion(name, num, code, month, time_info)
                    elif (month == "April") and ("April" in date):
                        if "April" not in activated_list:
                            april_courts()
                            startup_insertion(name, num, code, month, time_info)
                            activated_list.append("April")
                        else:
                            startup_insertion(name, num, code, month, time_info)
                    elif (month == "May") and ("May" in date):
                        if "May" not in activated_list:
                            may_courts()
                            startup_insertion(name, num, code, month, time_info)
                            activated_list.append("May")
                        else:
                            startup_insertion(name, num, code, month, time_info)
                    elif (month == "June") and ("June" in date):
                        if "June" not in activated_list:
                            june_courts()
                            startup_insertion(name, num, code, month, time_info)
                            activated_list.append("June")
                        else:
                            startup_insertion(name, num, code, month, time_info)
                    elif (month == "July") and ("July" in date):
                        if "July" not in activated_list:
                            july_courts()
                            startup_insertion(name, num, code, month, time_info)
                            activated_list.append("July")
                        else:
                            startup_insertion(name, num, code, month, time_info)
                    elif (month == "August") and ("August" in date):
                        if "August" not in activated_list:
                            august_courts()
                            startup_insertion(name, num, code, month, time_info)
                            activated_list.append("August")
                        else:
                            startup_insertion(name, num, code, month, time_info) 
                    elif (month == "September") and ("September" in date):
                        if "September" not in activated_list:
                            september_courts()
                            startup_insertion(name, num, code, month, time_info)
                            activated_list.append("September")
                        else:
                            startup_insertion(name, num, code, month, time_info)
                    elif (month == "October") and ("October" in date):
                        if "October" not in activated_list:
                            october_courts()
                            startup_insertion(name, num, code, month, time_info)
                            activated_list.append("October")
                        else:
                            startup_insertion(name, num, code, month, time_info)
                    elif (month == "November") and ("November" in date):
                        if "November" not in activated_list:
                            november_courts()
                            startup_insertion(name, num, code, month, time_info)
                            activated_list.append("November")
                        else:
                            startup_insertion(name, num, code, month, time_info)
                    elif (month == "December") and ("December" in date):
                        if "December" not in activated_list:
                            december_courts()
                            startup_insertion(name, num, code, month, time_info)
                            activated_list.append("December")
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
    img = Image.open(INSERT COMPANY LOGO IMAGE HERE)
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
            if input_month == "January":
                if "January" not in activated_list:
                    january_courts()
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                    activated_list.append("January")
                else:
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "February":
                if "February" not in activated_list:
                    february_courts()
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                    activated_list.append("February")
                else:
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "March":
                if "March" not in activated_list:
                    march_courts()
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                    activated_list.append("March")
                else:
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month == "April":
                if "April" not in activated_list:
                    april_courts()
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                    activated_list.append("April")
                else:
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month == "May":
                if "May" not in activated_list:
                    may_courts()
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                    activated_list.append("May")
                else:
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "June":
                if "June" not in activated_list:
                    june_courts()
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                    activated_list.append("June")
                else:
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "July":
                if "July" not in activated_list:
                    july_courts()
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                    activated_list.append("July")
                else:
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "August":
                if "August" not in activated_list:
                    august_courts()
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                    activated_list.append("August")
                else:
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "September":
                if "September" not in activated_list:
                    september_courts()
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                    activated_list.append("September")
                else:
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "October":
                if "October" not in activated_list:
                    october_courts()
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                    activated_list.append("October")
                else:
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "November":
                if "November" not in activated_list:
                    november_courts()
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                    activated_list.append("November")
                else:
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
            elif input_month ==  "December":
                if "December" not in activated_list:
                    december_courts()
                    for times in list_of_time_slots:
                        for court in court_num_list:
                            input_courtnum = int(court)
                            booking_insertion(input_name, input_num, input_month, input_day, times, input_courtnum, time_range, length_num)
                    activated_list.append("December")
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
    img = Image.open(INSERT COMPANY LOGO IMAGE HERE)
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
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=0)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=2)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=4)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=6)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=8)

        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 3, column=1)
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 6, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 9, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 12, column=1)
        court_number = Label(x, text="Court 1", bg= "lightblue", font=16).grid(row = 1, column=1)
        court_number = Label(x, text="Court 2", bg= "lightblue", font=16).grid(row = 4, column=1) 
        court_number = Label(x, text="Court 3", bg= "lightblue", font=16).grid(row = 7, column=1) 
        court_number = Label(x, text="Court 4", bg= "lightblue", font=16).grid(row = 10, column=1)
        court_number = Label(x, text="Court 5", bg= "lightblue", font=16).grid(row = 1, column=3)
        court_number = Label(x, text="Court 6", bg= "lightblue", font=16).grid(row = 4, column=3) 
        court_number = Label(x, text="Court 7", bg= "lightblue", font=16).grid(row = 7, column=3) 
        court_number = Label(x, text="Court 8", bg= "lightblue", font=16).grid(row = 10, column=3)
        court_number = Label(x, text="Court 9", bg= "lightblue", font=16).grid(row = 1, column=5)
        court_number = Label(x, text="Court 10", bg= "lightblue", font=16).grid(row = 4, column=5) 
        court_number = Label(x, text="Court 11", bg= "lightblue", font=16).grid(row = 7, column=5) 
        court_number = Label(x, text="Court 12", bg= "lightblue", font=16).grid(row = 10, column=5)
        court_number = Label(x, text="Court 13", bg= "lightblue", font=16).grid(row = 1, column=7)
        court_number = Label(x, text="Court 14", bg= "lightblue", font=16).grid(row = 4, column=7) 
        court_number = Label(x, text="Court 15", bg= "lightblue", font=16).grid(row = 7, column=7) 
        court_number = Label(x, text="Court 16", bg= "lightblue", font=16).grid(row = 10, column=7)
        court_number = Label(x, text="Court 17", bg= "lightblue", font=16).grid(row = 1, column=9)
        court_number = Label(x, text="Court 18", bg= "lightblue", font=16).grid(row = 4, column=9) 
        court_number = Label(x, text="Court 19", bg= "lightblue", font=16).grid(row = 7, column=9) 
        court_number = Label(x, text="Court 20", bg= "lightblue", font=16).grid(row = 10, column=9)

        court1 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court1.grid(row = 2, column=1)
        court2 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court2.grid(row = 5, column=1)
        court3 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court3.grid(row = 8, column=1)
        court4 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court4.grid(row = 11, column=1)
        court5 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court5.grid(row = 2, column=3)
        court6 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court6.grid(row = 5, column=3)
        court7 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court7.grid(row = 8, column=3)
        court8 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court8.grid(row = 11, column=3)
        court9 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court9.grid(row = 2, column=5)
        court10 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court10.grid(row = 5, column=5)
        court11 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court11.grid(row = 8, column=5)
        court12 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court12.grid(row = 11, column=5)
        court13 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court13.grid(row = 2, column=7)
        court14 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court14.grid(row = 5, column=7)
        court15 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court15.grid(row = 8, column=7)
        court16 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court16.grid(row = 11, column=7)
        court17 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court17.grid(row = 2, column=9)
        court18 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court18.grid(row = 5, column=9)
        court19 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court19.grid(row = 8, column=9)
        court20 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court20.grid(row = 11, column=9)

        jan_courtlist.append(court1)
        jan_courtlist.append(court2)
        jan_courtlist.append(court3)
        jan_courtlist.append(court4)
        jan_courtlist.append(court5)
        jan_courtlist.append(court6)
        jan_courtlist.append(court7)
        jan_courtlist.append(court8)
        jan_courtlist.append(court9)
        jan_courtlist.append(court10)
        jan_courtlist.append(court11)
        jan_courtlist.append(court12)
        jan_courtlist.append(court13)
        jan_courtlist.append(court14)
        jan_courtlist.append(court15)
        jan_courtlist.append(court16)
        jan_courtlist.append(court17)
        jan_courtlist.append(court18)
        jan_courtlist.append(court19)
        jan_courtlist.append(court20)

def february_courts():
    for x in court_times[744:1440]:
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=0)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=2)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=4)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=6)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=8)

        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 3, column=1)
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 6, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 9, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 12, column=1)
        court_number = Label(x, text="Court 1", bg= "lightblue", font=16).grid(row = 1, column=1)
        court_number = Label(x, text="Court 2", bg= "lightblue", font=16).grid(row = 4, column=1) 
        court_number = Label(x, text="Court 3", bg= "lightblue", font=16).grid(row = 7, column=1) 
        court_number = Label(x, text="Court 4", bg= "lightblue", font=16).grid(row = 10, column=1)
        court_number = Label(x, text="Court 5", bg= "lightblue", font=16).grid(row = 1, column=3)
        court_number = Label(x, text="Court 6", bg= "lightblue", font=16).grid(row = 4, column=3) 
        court_number = Label(x, text="Court 7", bg= "lightblue", font=16).grid(row = 7, column=3) 
        court_number = Label(x, text="Court 8", bg= "lightblue", font=16).grid(row = 10, column=3)
        court_number = Label(x, text="Court 9", bg= "lightblue", font=16).grid(row = 1, column=5)
        court_number = Label(x, text="Court 10", bg= "lightblue", font=16).grid(row = 4, column=5) 
        court_number = Label(x, text="Court 11", bg= "lightblue", font=16).grid(row = 7, column=5) 
        court_number = Label(x, text="Court 12", bg= "lightblue", font=16).grid(row = 10, column=5)
        court_number = Label(x, text="Court 13", bg= "lightblue", font=16).grid(row = 1, column=7)
        court_number = Label(x, text="Court 14", bg= "lightblue", font=16).grid(row = 4, column=7) 
        court_number = Label(x, text="Court 15", bg= "lightblue", font=16).grid(row = 7, column=7) 
        court_number = Label(x, text="Court 16", bg= "lightblue", font=16).grid(row = 10, column=7)
        court_number = Label(x, text="Court 17", bg= "lightblue", font=16).grid(row = 1, column=9)
        court_number = Label(x, text="Court 18", bg= "lightblue", font=16).grid(row = 4, column=9) 
        court_number = Label(x, text="Court 19", bg= "lightblue", font=16).grid(row = 7, column=9) 
        court_number = Label(x, text="Court 20", bg= "lightblue", font=16).grid(row = 10, column=9)
        
        court1 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court1.grid(row = 2, column=1)
        court2 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court2.grid(row = 5, column=1)
        court3 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court3.grid(row = 8, column=1)
        court4 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court4.grid(row = 11, column=1)
        court5 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court5.grid(row = 2, column=3)
        court6 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court6.grid(row = 5, column=3)
        court7 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court7.grid(row = 8, column=3)
        court8 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court8.grid(row = 11, column=3)
        court9 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court9.grid(row = 2, column=5)
        court10 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court10.grid(row = 5, column=5)
        court11 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court11.grid(row = 8, column=5)
        court12 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court12.grid(row = 11, column=5)
        court13 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court13.grid(row = 2, column=7)
        court14 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court14.grid(row = 5, column=7)
        court15 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court15.grid(row = 8, column=7)
        court16 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court16.grid(row = 11, column=7)
        court17 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court17.grid(row = 2, column=9)
        court18 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court18.grid(row = 5, column=9)
        court19 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court19.grid(row = 8, column=9)
        court20 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court20.grid(row = 11, column=9)

        feb_courtlist.append(court1)
        feb_courtlist.append(court2)
        feb_courtlist.append(court3)
        feb_courtlist.append(court4)
        feb_courtlist.append(court5)
        feb_courtlist.append(court6)
        feb_courtlist.append(court7)
        feb_courtlist.append(court8)
        feb_courtlist.append(court9)
        feb_courtlist.append(court10)
        feb_courtlist.append(court11)
        feb_courtlist.append(court12)
        feb_courtlist.append(court13)
        feb_courtlist.append(court14)
        feb_courtlist.append(court15)
        feb_courtlist.append(court16)
        feb_courtlist.append(court17)
        feb_courtlist.append(court18)
        feb_courtlist.append(court19)
        feb_courtlist.append(court20)

def march_courts():
    for x in court_times[1440:2184]:
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=0)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=2)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=4)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=6)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=8)

        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 3, column=1)
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 6, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 9, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 12, column=1)
        court_number = Label(x, text="Court 1", bg= "lightblue", font=16).grid(row = 1, column=1)
        court_number = Label(x, text="Court 2", bg= "lightblue", font=16).grid(row = 4, column=1) 
        court_number = Label(x, text="Court 3", bg= "lightblue", font=16).grid(row = 7, column=1) 
        court_number = Label(x, text="Court 4", bg= "lightblue", font=16).grid(row = 10, column=1)
        court_number = Label(x, text="Court 5", bg= "lightblue", font=16).grid(row = 1, column=3)
        court_number = Label(x, text="Court 6", bg= "lightblue", font=16).grid(row = 4, column=3) 
        court_number = Label(x, text="Court 7", bg= "lightblue", font=16).grid(row = 7, column=3) 
        court_number = Label(x, text="Court 8", bg= "lightblue", font=16).grid(row = 10, column=3)
        court_number = Label(x, text="Court 9", bg= "lightblue", font=16).grid(row = 1, column=5)
        court_number = Label(x, text="Court 10", bg= "lightblue", font=16).grid(row = 4, column=5) 
        court_number = Label(x, text="Court 11", bg= "lightblue", font=16).grid(row = 7, column=5) 
        court_number = Label(x, text="Court 12", bg= "lightblue", font=16).grid(row = 10, column=5)
        court_number = Label(x, text="Court 13", bg= "lightblue", font=16).grid(row = 1, column=7)
        court_number = Label(x, text="Court 14", bg= "lightblue", font=16).grid(row = 4, column=7) 
        court_number = Label(x, text="Court 15", bg= "lightblue", font=16).grid(row = 7, column=7) 
        court_number = Label(x, text="Court 16", bg= "lightblue", font=16).grid(row = 10, column=7)
        court_number = Label(x, text="Court 17", bg= "lightblue", font=16).grid(row = 1, column=9)
        court_number = Label(x, text="Court 18", bg= "lightblue", font=16).grid(row = 4, column=9) 
        court_number = Label(x, text="Court 19", bg= "lightblue", font=16).grid(row = 7, column=9) 
        court_number = Label(x, text="Court 20", bg= "lightblue", font=16).grid(row = 10, column=9)
        
        court1 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court1.grid(row = 2, column=1)
        court2 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court2.grid(row = 5, column=1)
        court3 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court3.grid(row = 8, column=1)
        court4 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court4.grid(row = 11, column=1)
        court5 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court5.grid(row = 2, column=3)
        court6 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court6.grid(row = 5, column=3)
        court7 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court7.grid(row = 8, column=3)
        court8 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court8.grid(row = 11, column=3)
        court9 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court9.grid(row = 2, column=5)
        court10 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court10.grid(row = 5, column=5)
        court11 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court11.grid(row = 8, column=5)
        court12 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court12.grid(row = 11, column=5)
        court13 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court13.grid(row = 2, column=7)
        court14 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court14.grid(row = 5, column=7)
        court15 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court15.grid(row = 8, column=7)
        court16 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court16.grid(row = 11, column=7)
        court17 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court17.grid(row = 2, column=9)
        court18 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court18.grid(row = 5, column=9)
        court19 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court19.grid(row = 8, column=9)
        court20 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court20.grid(row = 11, column=9)

        mar_courtlist.append(court1)
        mar_courtlist.append(court2)
        mar_courtlist.append(court3)
        mar_courtlist.append(court4)
        mar_courtlist.append(court5)
        mar_courtlist.append(court6)
        mar_courtlist.append(court7)
        mar_courtlist.append(court8)
        mar_courtlist.append(court9)
        mar_courtlist.append(court10)
        mar_courtlist.append(court11)
        mar_courtlist.append(court12)
        mar_courtlist.append(court13)
        mar_courtlist.append(court14)
        mar_courtlist.append(court15)
        mar_courtlist.append(court16)
        mar_courtlist.append(court17)
        mar_courtlist.append(court18)
        mar_courtlist.append(court19)
        mar_courtlist.append(court20)

def april_courts():
    for x in court_times[2184:2904]:
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=0)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=2)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=4)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=6)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=8)

        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 3, column=1)
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 6, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 9, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 12, column=1)
        court_number = Label(x, text="Court 1", bg= "lightblue", font=16).grid(row = 1, column=1)
        court_number = Label(x, text="Court 2", bg= "lightblue", font=16).grid(row = 4, column=1) 
        court_number = Label(x, text="Court 3", bg= "lightblue", font=16).grid(row = 7, column=1) 
        court_number = Label(x, text="Court 4", bg= "lightblue", font=16).grid(row = 10, column=1)
        court_number = Label(x, text="Court 5", bg= "lightblue", font=16).grid(row = 1, column=3)
        court_number = Label(x, text="Court 6", bg= "lightblue", font=16).grid(row = 4, column=3) 
        court_number = Label(x, text="Court 7", bg= "lightblue", font=16).grid(row = 7, column=3) 
        court_number = Label(x, text="Court 8", bg= "lightblue", font=16).grid(row = 10, column=3)
        court_number = Label(x, text="Court 9", bg= "lightblue", font=16).grid(row = 1, column=5)
        court_number = Label(x, text="Court 10", bg= "lightblue", font=16).grid(row = 4, column=5) 
        court_number = Label(x, text="Court 11", bg= "lightblue", font=16).grid(row = 7, column=5) 
        court_number = Label(x, text="Court 12", bg= "lightblue", font=16).grid(row = 10, column=5)
        court_number = Label(x, text="Court 13", bg= "lightblue", font=16).grid(row = 1, column=7)
        court_number = Label(x, text="Court 14", bg= "lightblue", font=16).grid(row = 4, column=7) 
        court_number = Label(x, text="Court 15", bg= "lightblue", font=16).grid(row = 7, column=7) 
        court_number = Label(x, text="Court 16", bg= "lightblue", font=16).grid(row = 10, column=7)
        court_number = Label(x, text="Court 17", bg= "lightblue", font=16).grid(row = 1, column=9)
        court_number = Label(x, text="Court 18", bg= "lightblue", font=16).grid(row = 4, column=9) 
        court_number = Label(x, text="Court 19", bg= "lightblue", font=16).grid(row = 7, column=9) 
        court_number = Label(x, text="Court 20", bg= "lightblue", font=16).grid(row = 10, column=9)
        
        court1 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court1.grid(row = 2, column=1)
        court2 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court2.grid(row = 5, column=1)
        court3 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court3.grid(row = 8, column=1)
        court4 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court4.grid(row = 11, column=1)
        court5 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court5.grid(row = 2, column=3)
        court6 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court6.grid(row = 5, column=3)
        court7 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court7.grid(row = 8, column=3)
        court8 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court8.grid(row = 11, column=3)
        court9 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court9.grid(row = 2, column=5)
        court10 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court10.grid(row = 5, column=5)
        court11 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court11.grid(row = 8, column=5)
        court12 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court12.grid(row = 11, column=5)
        court13 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court13.grid(row = 2, column=7)
        court14 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court14.grid(row = 5, column=7)
        court15 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court15.grid(row = 8, column=7)
        court16 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court16.grid(row = 11, column=7)
        court17 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court17.grid(row = 2, column=9)
        court18 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court18.grid(row = 5, column=9)
        court19 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court19.grid(row = 8, column=9)
        court20 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court20.grid(row = 11, column=9)

        apr_courtlist.append(court1)
        apr_courtlist.append(court2)
        apr_courtlist.append(court3)
        apr_courtlist.append(court4)
        apr_courtlist.append(court5)
        apr_courtlist.append(court6)
        apr_courtlist.append(court7)
        apr_courtlist.append(court8)
        apr_courtlist.append(court9)
        apr_courtlist.append(court10)
        apr_courtlist.append(court11)
        apr_courtlist.append(court12)
        apr_courtlist.append(court13)
        apr_courtlist.append(court14)
        apr_courtlist.append(court15)
        apr_courtlist.append(court16)
        apr_courtlist.append(court17)
        apr_courtlist.append(court18)
        apr_courtlist.append(court19)
        apr_courtlist.append(court20)


def may_courts():
    for x in court_times[2904:3648]:
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=0)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=2)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=4)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=6)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=8)

        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 3, column=1)
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 6, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 9, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 12, column=1)
        court_number = Label(x, text="Court 1", bg= "lightblue", font=16).grid(row = 1, column=1)
        court_number = Label(x, text="Court 2", bg= "lightblue", font=16).grid(row = 4, column=1) 
        court_number = Label(x, text="Court 3", bg= "lightblue", font=16).grid(row = 7, column=1) 
        court_number = Label(x, text="Court 4", bg= "lightblue", font=16).grid(row = 10, column=1)
        court_number = Label(x, text="Court 5", bg= "lightblue", font=16).grid(row = 1, column=3)
        court_number = Label(x, text="Court 6", bg= "lightblue", font=16).grid(row = 4, column=3) 
        court_number = Label(x, text="Court 7", bg= "lightblue", font=16).grid(row = 7, column=3) 
        court_number = Label(x, text="Court 8", bg= "lightblue", font=16).grid(row = 10, column=3)
        court_number = Label(x, text="Court 9", bg= "lightblue", font=16).grid(row = 1, column=5)
        court_number = Label(x, text="Court 10", bg= "lightblue", font=16).grid(row = 4, column=5) 
        court_number = Label(x, text="Court 11", bg= "lightblue", font=16).grid(row = 7, column=5) 
        court_number = Label(x, text="Court 12", bg= "lightblue", font=16).grid(row = 10, column=5)
        court_number = Label(x, text="Court 13", bg= "lightblue", font=16).grid(row = 1, column=7)
        court_number = Label(x, text="Court 14", bg= "lightblue", font=16).grid(row = 4, column=7) 
        court_number = Label(x, text="Court 15", bg= "lightblue", font=16).grid(row = 7, column=7) 
        court_number = Label(x, text="Court 16", bg= "lightblue", font=16).grid(row = 10, column=7)
        court_number = Label(x, text="Court 17", bg= "lightblue", font=16).grid(row = 1, column=9)
        court_number = Label(x, text="Court 18", bg= "lightblue", font=16).grid(row = 4, column=9) 
        court_number = Label(x, text="Court 19", bg= "lightblue", font=16).grid(row = 7, column=9) 
        court_number = Label(x, text="Court 20", bg= "lightblue", font=16).grid(row = 10, column=9)
        
        court1 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court1.grid(row = 2, column=1)
        court2 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court2.grid(row = 5, column=1)
        court3 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court3.grid(row = 8, column=1)
        court4 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court4.grid(row = 11, column=1)
        court5 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court5.grid(row = 2, column=3)
        court6 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court6.grid(row = 5, column=3)
        court7 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court7.grid(row = 8, column=3)
        court8 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court8.grid(row = 11, column=3)
        court9 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court9.grid(row = 2, column=5)
        court10 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court10.grid(row = 5, column=5)
        court11 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court11.grid(row = 8, column=5)
        court12 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court12.grid(row = 11, column=5)
        court13 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court13.grid(row = 2, column=7)
        court14 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court14.grid(row = 5, column=7)
        court15 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court15.grid(row = 8, column=7)
        court16 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court16.grid(row = 11, column=7)
        court17 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court17.grid(row = 2, column=9)
        court18 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court18.grid(row = 5, column=9)
        court19 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court19.grid(row = 8, column=9)
        court20 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court20.grid(row = 11, column=9)

        may_courtlist.append(court1)
        may_courtlist.append(court2)
        may_courtlist.append(court3)
        may_courtlist.append(court4)
        may_courtlist.append(court5)
        may_courtlist.append(court6)
        may_courtlist.append(court7)
        may_courtlist.append(court8)
        may_courtlist.append(court9)
        may_courtlist.append(court10)
        may_courtlist.append(court11)
        may_courtlist.append(court12)
        may_courtlist.append(court13)
        may_courtlist.append(court14)
        may_courtlist.append(court15)
        may_courtlist.append(court16)
        may_courtlist.append(court17)
        may_courtlist.append(court18)
        may_courtlist.append(court19)
        may_courtlist.append(court20)



def june_courts():
    for x in court_times[3648:4368]:
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=0)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=2)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=4)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=6)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=8)

        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 3, column=1)
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 6, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 9, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 12, column=1)
        court_number = Label(x, text="Court 1", bg= "lightblue", font=16).grid(row = 1, column=1)
        court_number = Label(x, text="Court 2", bg= "lightblue", font=16).grid(row = 4, column=1) 
        court_number = Label(x, text="Court 3", bg= "lightblue", font=16).grid(row = 7, column=1) 
        court_number = Label(x, text="Court 4", bg= "lightblue", font=16).grid(row = 10, column=1)
        court_number = Label(x, text="Court 5", bg= "lightblue", font=16).grid(row = 1, column=3)
        court_number = Label(x, text="Court 6", bg= "lightblue", font=16).grid(row = 4, column=3) 
        court_number = Label(x, text="Court 7", bg= "lightblue", font=16).grid(row = 7, column=3) 
        court_number = Label(x, text="Court 8", bg= "lightblue", font=16).grid(row = 10, column=3)
        court_number = Label(x, text="Court 9", bg= "lightblue", font=16).grid(row = 1, column=5)
        court_number = Label(x, text="Court 10", bg= "lightblue", font=16).grid(row = 4, column=5) 
        court_number = Label(x, text="Court 11", bg= "lightblue", font=16).grid(row = 7, column=5) 
        court_number = Label(x, text="Court 12", bg= "lightblue", font=16).grid(row = 10, column=5)
        court_number = Label(x, text="Court 13", bg= "lightblue", font=16).grid(row = 1, column=7)
        court_number = Label(x, text="Court 14", bg= "lightblue", font=16).grid(row = 4, column=7) 
        court_number = Label(x, text="Court 15", bg= "lightblue", font=16).grid(row = 7, column=7) 
        court_number = Label(x, text="Court 16", bg= "lightblue", font=16).grid(row = 10, column=7)
        court_number = Label(x, text="Court 17", bg= "lightblue", font=16).grid(row = 1, column=9)
        court_number = Label(x, text="Court 18", bg= "lightblue", font=16).grid(row = 4, column=9) 
        court_number = Label(x, text="Court 19", bg= "lightblue", font=16).grid(row = 7, column=9) 
        court_number = Label(x, text="Court 20", bg= "lightblue", font=16).grid(row = 10, column=9)
        
        court1 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court1.grid(row = 2, column=1)
        court2 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court2.grid(row = 5, column=1)
        court3 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court3.grid(row = 8, column=1)
        court4 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court4.grid(row = 11, column=1)
        court5 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court5.grid(row = 2, column=3)
        court6 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court6.grid(row = 5, column=3)
        court7 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court7.grid(row = 8, column=3)
        court8 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court8.grid(row = 11, column=3)
        court9 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court9.grid(row = 2, column=5)
        court10 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court10.grid(row = 5, column=5)
        court11 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court11.grid(row = 8, column=5)
        court12 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court12.grid(row = 11, column=5)
        court13 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court13.grid(row = 2, column=7)
        court14 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court14.grid(row = 5, column=7)
        court15 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court15.grid(row = 8, column=7)
        court16 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court16.grid(row = 11, column=7)
        court17 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court17.grid(row = 2, column=9)
        court18 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court18.grid(row = 5, column=9)
        court19 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court19.grid(row = 8, column=9)
        court20 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court20.grid(row = 11, column=9)

        jun_courtlist.append(court1)
        jun_courtlist.append(court2)
        jun_courtlist.append(court3)
        jun_courtlist.append(court4)
        jun_courtlist.append(court5)
        jun_courtlist.append(court6)
        jun_courtlist.append(court7)
        jun_courtlist.append(court8)
        jun_courtlist.append(court9)
        jun_courtlist.append(court10)
        jun_courtlist.append(court11)
        jun_courtlist.append(court12)
        jun_courtlist.append(court13)
        jun_courtlist.append(court14)
        jun_courtlist.append(court15)
        jun_courtlist.append(court16)
        jun_courtlist.append(court17)
        jun_courtlist.append(court18)
        jun_courtlist.append(court19)
        jun_courtlist.append(court20)


def july_courts():
    for x in court_times[4368:5112]:
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=0)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=2)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=4)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=6)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=8)

        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 3, column=1)
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 6, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 9, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 12, column=1)
        court_number = Label(x, text="Court 1", bg= "lightblue", font=16).grid(row = 1, column=1)
        court_number = Label(x, text="Court 2", bg= "lightblue", font=16).grid(row = 4, column=1) 
        court_number = Label(x, text="Court 3", bg= "lightblue", font=16).grid(row = 7, column=1) 
        court_number = Label(x, text="Court 4", bg= "lightblue", font=16).grid(row = 10, column=1)
        court_number = Label(x, text="Court 5", bg= "lightblue", font=16).grid(row = 1, column=3)
        court_number = Label(x, text="Court 6", bg= "lightblue", font=16).grid(row = 4, column=3) 
        court_number = Label(x, text="Court 7", bg= "lightblue", font=16).grid(row = 7, column=3) 
        court_number = Label(x, text="Court 8", bg= "lightblue", font=16).grid(row = 10, column=3)
        court_number = Label(x, text="Court 9", bg= "lightblue", font=16).grid(row = 1, column=5)
        court_number = Label(x, text="Court 10", bg= "lightblue", font=16).grid(row = 4, column=5) 
        court_number = Label(x, text="Court 11", bg= "lightblue", font=16).grid(row = 7, column=5) 
        court_number = Label(x, text="Court 12", bg= "lightblue", font=16).grid(row = 10, column=5)
        court_number = Label(x, text="Court 13", bg= "lightblue", font=16).grid(row = 1, column=7)
        court_number = Label(x, text="Court 14", bg= "lightblue", font=16).grid(row = 4, column=7) 
        court_number = Label(x, text="Court 15", bg= "lightblue", font=16).grid(row = 7, column=7) 
        court_number = Label(x, text="Court 16", bg= "lightblue", font=16).grid(row = 10, column=7)
        court_number = Label(x, text="Court 17", bg= "lightblue", font=16).grid(row = 1, column=9)
        court_number = Label(x, text="Court 18", bg= "lightblue", font=16).grid(row = 4, column=9) 
        court_number = Label(x, text="Court 19", bg= "lightblue", font=16).grid(row = 7, column=9) 
        court_number = Label(x, text="Court 20", bg= "lightblue", font=16).grid(row = 10, column=9)
        
        court1 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court1.grid(row = 2, column=1)
        court2 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court2.grid(row = 5, column=1)
        court3 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court3.grid(row = 8, column=1)
        court4 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court4.grid(row = 11, column=1)
        court5 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court5.grid(row = 2, column=3)
        court6 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court6.grid(row = 5, column=3)
        court7 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court7.grid(row = 8, column=3)
        court8 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court8.grid(row = 11, column=3)
        court9 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court9.grid(row = 2, column=5)
        court10 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court10.grid(row = 5, column=5)
        court11 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court11.grid(row = 8, column=5)
        court12 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court12.grid(row = 11, column=5)
        court13 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court13.grid(row = 2, column=7)
        court14 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court14.grid(row = 5, column=7)
        court15 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court15.grid(row = 8, column=7)
        court16 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court16.grid(row = 11, column=7)
        court17 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court17.grid(row = 2, column=9)
        court18 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court18.grid(row = 5, column=9)
        court19 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court19.grid(row = 8, column=9)
        court20 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court20.grid(row = 11, column=9)

        jul_courtlist.append(court1)
        jul_courtlist.append(court2)
        jul_courtlist.append(court3)
        jul_courtlist.append(court4)
        jul_courtlist.append(court5)
        jul_courtlist.append(court6)
        jul_courtlist.append(court7)
        jul_courtlist.append(court8)
        jul_courtlist.append(court9)
        jul_courtlist.append(court10)
        jul_courtlist.append(court11)
        jul_courtlist.append(court12)
        jul_courtlist.append(court13)
        jul_courtlist.append(court14)
        jul_courtlist.append(court15)
        jul_courtlist.append(court16)
        jul_courtlist.append(court17)
        jul_courtlist.append(court18)
        jul_courtlist.append(court19)
        jul_courtlist.append(court20)

def august_courts():
    for x in court_times[5112:5856]:
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=0)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=2)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=4)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=6)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=8)

        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 3, column=1)
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 6, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 9, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 12, column=1)
        court_number = Label(x, text="Court 1", bg= "lightblue", font=16).grid(row = 1, column=1)
        court_number = Label(x, text="Court 2", bg= "lightblue", font=16).grid(row = 4, column=1) 
        court_number = Label(x, text="Court 3", bg= "lightblue", font=16).grid(row = 7, column=1) 
        court_number = Label(x, text="Court 4", bg= "lightblue", font=16).grid(row = 10, column=1)
        court_number = Label(x, text="Court 5", bg= "lightblue", font=16).grid(row = 1, column=3)
        court_number = Label(x, text="Court 6", bg= "lightblue", font=16).grid(row = 4, column=3) 
        court_number = Label(x, text="Court 7", bg= "lightblue", font=16).grid(row = 7, column=3) 
        court_number = Label(x, text="Court 8", bg= "lightblue", font=16).grid(row = 10, column=3)
        court_number = Label(x, text="Court 9", bg= "lightblue", font=16).grid(row = 1, column=5)
        court_number = Label(x, text="Court 10", bg= "lightblue", font=16).grid(row = 4, column=5) 
        court_number = Label(x, text="Court 11", bg= "lightblue", font=16).grid(row = 7, column=5) 
        court_number = Label(x, text="Court 12", bg= "lightblue", font=16).grid(row = 10, column=5)
        court_number = Label(x, text="Court 13", bg= "lightblue", font=16).grid(row = 1, column=7)
        court_number = Label(x, text="Court 14", bg= "lightblue", font=16).grid(row = 4, column=7) 
        court_number = Label(x, text="Court 15", bg= "lightblue", font=16).grid(row = 7, column=7) 
        court_number = Label(x, text="Court 16", bg= "lightblue", font=16).grid(row = 10, column=7)
        court_number = Label(x, text="Court 17", bg= "lightblue", font=16).grid(row = 1, column=9)
        court_number = Label(x, text="Court 18", bg= "lightblue", font=16).grid(row = 4, column=9) 
        court_number = Label(x, text="Court 19", bg= "lightblue", font=16).grid(row = 7, column=9) 
        court_number = Label(x, text="Court 20", bg= "lightblue", font=16).grid(row = 10, column=9)
        
        court1 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court1.grid(row = 2, column=1)
        court2 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court2.grid(row = 5, column=1)
        court3 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court3.grid(row = 8, column=1)
        court4 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court4.grid(row = 11, column=1)
        court5 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court5.grid(row = 2, column=3)
        court6 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court6.grid(row = 5, column=3)
        court7 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court7.grid(row = 8, column=3)
        court8 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court8.grid(row = 11, column=3)
        court9 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court9.grid(row = 2, column=5)
        court10 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court10.grid(row = 5, column=5)
        court11 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court11.grid(row = 8, column=5)
        court12 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court12.grid(row = 11, column=5)
        court13 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court13.grid(row = 2, column=7)
        court14 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court14.grid(row = 5, column=7)
        court15 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court15.grid(row = 8, column=7)
        court16 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court16.grid(row = 11, column=7)
        court17 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court17.grid(row = 2, column=9)
        court18 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court18.grid(row = 5, column=9)
        court19 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court19.grid(row = 8, column=9)
        court20 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court20.grid(row = 11, column=9)

        aug_courtlist.append(court1)
        aug_courtlist.append(court2)
        aug_courtlist.append(court3)
        aug_courtlist.append(court4)
        aug_courtlist.append(court5)
        aug_courtlist.append(court6)
        aug_courtlist.append(court7)
        aug_courtlist.append(court8)
        aug_courtlist.append(court9)
        aug_courtlist.append(court10)
        aug_courtlist.append(court11)
        aug_courtlist.append(court12)
        aug_courtlist.append(court13)
        aug_courtlist.append(court14)
        aug_courtlist.append(court15)
        aug_courtlist.append(court16)
        aug_courtlist.append(court17)
        aug_courtlist.append(court18)
        aug_courtlist.append(court19)
        aug_courtlist.append(court20)

def september_courts():
    for x in court_times[5856:6576]:
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=0)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=2)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=4)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=6)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=8)

        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 3, column=1)
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 6, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 9, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 12, column=1)
        court_number = Label(x, text="Court 1", bg= "lightblue", font=16).grid(row = 1, column=1)
        court_number = Label(x, text="Court 2", bg= "lightblue", font=16).grid(row = 4, column=1) 
        court_number = Label(x, text="Court 3", bg= "lightblue", font=16).grid(row = 7, column=1) 
        court_number = Label(x, text="Court 4", bg= "lightblue", font=16).grid(row = 10, column=1)
        court_number = Label(x, text="Court 5", bg= "lightblue", font=16).grid(row = 1, column=3)
        court_number = Label(x, text="Court 6", bg= "lightblue", font=16).grid(row = 4, column=3) 
        court_number = Label(x, text="Court 7", bg= "lightblue", font=16).grid(row = 7, column=3) 
        court_number = Label(x, text="Court 8", bg= "lightblue", font=16).grid(row = 10, column=3)
        court_number = Label(x, text="Court 9", bg= "lightblue", font=16).grid(row = 1, column=5)
        court_number = Label(x, text="Court 10", bg= "lightblue", font=16).grid(row = 4, column=5) 
        court_number = Label(x, text="Court 11", bg= "lightblue", font=16).grid(row = 7, column=5) 
        court_number = Label(x, text="Court 12", bg= "lightblue", font=16).grid(row = 10, column=5)
        court_number = Label(x, text="Court 13", bg= "lightblue", font=16).grid(row = 1, column=7)
        court_number = Label(x, text="Court 14", bg= "lightblue", font=16).grid(row = 4, column=7) 
        court_number = Label(x, text="Court 15", bg= "lightblue", font=16).grid(row = 7, column=7) 
        court_number = Label(x, text="Court 16", bg= "lightblue", font=16).grid(row = 10, column=7)
        court_number = Label(x, text="Court 17", bg= "lightblue", font=16).grid(row = 1, column=9)
        court_number = Label(x, text="Court 18", bg= "lightblue", font=16).grid(row = 4, column=9) 
        court_number = Label(x, text="Court 19", bg= "lightblue", font=16).grid(row = 7, column=9) 
        court_number = Label(x, text="Court 20", bg= "lightblue", font=16).grid(row = 10, column=9)
        
        court1 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court1.grid(row = 2, column=1)
        court2 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court2.grid(row = 5, column=1)
        court3 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court3.grid(row = 8, column=1)
        court4 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court4.grid(row = 11, column=1)
        court5 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court5.grid(row = 2, column=3)
        court6 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court6.grid(row = 5, column=3)
        court7 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court7.grid(row = 8, column=3)
        court8 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court8.grid(row = 11, column=3)
        court9 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court9.grid(row = 2, column=5)
        court10 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court10.grid(row = 5, column=5)
        court11 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court11.grid(row = 8, column=5)
        court12 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court12.grid(row = 11, column=5)
        court13 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court13.grid(row = 2, column=7)
        court14 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court14.grid(row = 5, column=7)
        court15 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court15.grid(row = 8, column=7)
        court16 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court16.grid(row = 11, column=7)
        court17 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court17.grid(row = 2, column=9)
        court18 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court18.grid(row = 5, column=9)
        court19 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court19.grid(row = 8, column=9)
        court20 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court20.grid(row = 11, column=9)

        sep_courtlist.append(court1)
        sep_courtlist.append(court2)
        sep_courtlist.append(court3)
        sep_courtlist.append(court4)
        sep_courtlist.append(court5)
        sep_courtlist.append(court6)
        sep_courtlist.append(court7)
        sep_courtlist.append(court8)
        sep_courtlist.append(court9)
        sep_courtlist.append(court10)
        sep_courtlist.append(court11)
        sep_courtlist.append(court12)
        sep_courtlist.append(court13)
        sep_courtlist.append(court14)
        sep_courtlist.append(court15)
        sep_courtlist.append(court16)
        sep_courtlist.append(court17)
        sep_courtlist.append(court18)
        sep_courtlist.append(court19)
        sep_courtlist.append(court20)

def october_courts():
    for x in court_times[6576:7320]:
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=0)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=2)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=4)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=6)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=8)

        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 3, column=1)
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 6, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 9, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 12, column=1)
        court_number = Label(x, text="Court 1", bg= "lightblue", font=16).grid(row = 1, column=1)
        court_number = Label(x, text="Court 2", bg= "lightblue", font=16).grid(row = 4, column=1) 
        court_number = Label(x, text="Court 3", bg= "lightblue", font=16).grid(row = 7, column=1) 
        court_number = Label(x, text="Court 4", bg= "lightblue", font=16).grid(row = 10, column=1)
        court_number = Label(x, text="Court 5", bg= "lightblue", font=16).grid(row = 1, column=3)
        court_number = Label(x, text="Court 6", bg= "lightblue", font=16).grid(row = 4, column=3) 
        court_number = Label(x, text="Court 7", bg= "lightblue", font=16).grid(row = 7, column=3) 
        court_number = Label(x, text="Court 8", bg= "lightblue", font=16).grid(row = 10, column=3)
        court_number = Label(x, text="Court 9", bg= "lightblue", font=16).grid(row = 1, column=5)
        court_number = Label(x, text="Court 10", bg= "lightblue", font=16).grid(row = 4, column=5) 
        court_number = Label(x, text="Court 11", bg= "lightblue", font=16).grid(row = 7, column=5) 
        court_number = Label(x, text="Court 12", bg= "lightblue", font=16).grid(row = 10, column=5)
        court_number = Label(x, text="Court 13", bg= "lightblue", font=16).grid(row = 1, column=7)
        court_number = Label(x, text="Court 14", bg= "lightblue", font=16).grid(row = 4, column=7) 
        court_number = Label(x, text="Court 15", bg= "lightblue", font=16).grid(row = 7, column=7) 
        court_number = Label(x, text="Court 16", bg= "lightblue", font=16).grid(row = 10, column=7)
        court_number = Label(x, text="Court 17", bg= "lightblue", font=16).grid(row = 1, column=9)
        court_number = Label(x, text="Court 18", bg= "lightblue", font=16).grid(row = 4, column=9) 
        court_number = Label(x, text="Court 19", bg= "lightblue", font=16).grid(row = 7, column=9) 
        court_number = Label(x, text="Court 20", bg= "lightblue", font=16).grid(row = 10, column=9)
        
        court1 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court1.grid(row = 2, column=1)
        court2 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court2.grid(row = 5, column=1)
        court3 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court3.grid(row = 8, column=1)
        court4 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court4.grid(row = 11, column=1)
        court5 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court5.grid(row = 2, column=3)
        court6 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court6.grid(row = 5, column=3)
        court7 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court7.grid(row = 8, column=3)
        court8 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court8.grid(row = 11, column=3)
        court9 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court9.grid(row = 2, column=5)
        court10 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court10.grid(row = 5, column=5)
        court11 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court11.grid(row = 8, column=5)
        court12 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court12.grid(row = 11, column=5)
        court13 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court13.grid(row = 2, column=7)
        court14 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court14.grid(row = 5, column=7)
        court15 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court15.grid(row = 8, column=7)
        court16 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court16.grid(row = 11, column=7)
        court17 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court17.grid(row = 2, column=9)
        court18 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court18.grid(row = 5, column=9)
        court19 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court19.grid(row = 8, column=9)
        court20 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court20.grid(row = 11, column=9)

        oct_courtlist.append(court1)
        oct_courtlist.append(court2)
        oct_courtlist.append(court3)
        oct_courtlist.append(court4)
        oct_courtlist.append(court5)
        oct_courtlist.append(court6)
        oct_courtlist.append(court7)
        oct_courtlist.append(court8)
        oct_courtlist.append(court9)
        oct_courtlist.append(court10)
        oct_courtlist.append(court11)
        oct_courtlist.append(court12)
        oct_courtlist.append(court13)
        oct_courtlist.append(court14)
        oct_courtlist.append(court15)
        oct_courtlist.append(court16)
        oct_courtlist.append(court17)
        oct_courtlist.append(court18)
        oct_courtlist.append(court19)
        oct_courtlist.append(court20)

def november_courts():
    for x in court_times[7320:8040]:
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=0)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=2)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=4)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=6)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=8)

        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 3, column=1)
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 6, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 9, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 12, column=1)
        court_number = Label(x, text="Court 1", bg= "lightblue", font=16).grid(row = 1, column=1)
        court_number = Label(x, text="Court 2", bg= "lightblue", font=16).grid(row = 4, column=1) 
        court_number = Label(x, text="Court 3", bg= "lightblue", font=16).grid(row = 7, column=1) 
        court_number = Label(x, text="Court 4", bg= "lightblue", font=16).grid(row = 10, column=1)
        court_number = Label(x, text="Court 5", bg= "lightblue", font=16).grid(row = 1, column=3)
        court_number = Label(x, text="Court 6", bg= "lightblue", font=16).grid(row = 4, column=3) 
        court_number = Label(x, text="Court 7", bg= "lightblue", font=16).grid(row = 7, column=3) 
        court_number = Label(x, text="Court 8", bg= "lightblue", font=16).grid(row = 10, column=3)
        court_number = Label(x, text="Court 9", bg= "lightblue", font=16).grid(row = 1, column=5)
        court_number = Label(x, text="Court 10", bg= "lightblue", font=16).grid(row = 4, column=5) 
        court_number = Label(x, text="Court 11", bg= "lightblue", font=16).grid(row = 7, column=5) 
        court_number = Label(x, text="Court 12", bg= "lightblue", font=16).grid(row = 10, column=5)
        court_number = Label(x, text="Court 13", bg= "lightblue", font=16).grid(row = 1, column=7)
        court_number = Label(x, text="Court 14", bg= "lightblue", font=16).grid(row = 4, column=7) 
        court_number = Label(x, text="Court 15", bg= "lightblue", font=16).grid(row = 7, column=7) 
        court_number = Label(x, text="Court 16", bg= "lightblue", font=16).grid(row = 10, column=7)
        court_number = Label(x, text="Court 17", bg= "lightblue", font=16).grid(row = 1, column=9)
        court_number = Label(x, text="Court 18", bg= "lightblue", font=16).grid(row = 4, column=9) 
        court_number = Label(x, text="Court 19", bg= "lightblue", font=16).grid(row = 7, column=9) 
        court_number = Label(x, text="Court 20", bg= "lightblue", font=16).grid(row = 10, column=9)
        
        court1 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court1.grid(row = 2, column=1)
        court2 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court2.grid(row = 5, column=1)
        court3 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court3.grid(row = 8, column=1)
        court4 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court4.grid(row = 11, column=1)
        court5 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court5.grid(row = 2, column=3)
        court6 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court6.grid(row = 5, column=3)
        court7 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court7.grid(row = 8, column=3)
        court8 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court8.grid(row = 11, column=3)
        court9 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court9.grid(row = 2, column=5)
        court10 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court10.grid(row = 5, column=5)
        court11 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court11.grid(row = 8, column=5)
        court12 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court12.grid(row = 11, column=5)
        court13 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court13.grid(row = 2, column=7)
        court14 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court14.grid(row = 5, column=7)
        court15 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court15.grid(row = 8, column=7)
        court16 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court16.grid(row = 11, column=7)
        court17 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court17.grid(row = 2, column=9)
        court18 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court18.grid(row = 5, column=9)
        court19 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court19.grid(row = 8, column=9)
        court20 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court20.grid(row = 11, column=9)

        nov_courtlist.append(court1)
        nov_courtlist.append(court2)
        nov_courtlist.append(court3)
        nov_courtlist.append(court4)
        nov_courtlist.append(court5)
        nov_courtlist.append(court6)
        nov_courtlist.append(court7)
        nov_courtlist.append(court8)
        nov_courtlist.append(court9)
        nov_courtlist.append(court10)
        nov_courtlist.append(court11)
        nov_courtlist.append(court12)
        nov_courtlist.append(court13)
        nov_courtlist.append(court14)
        nov_courtlist.append(court15)
        nov_courtlist.append(court16)
        nov_courtlist.append(court17)
        nov_courtlist.append(court18)
        nov_courtlist.append(court19)
        nov_courtlist.append(court20)

def december_courts():
    for x in court_times[8040:8784]:
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=0)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=2)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=4)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=6)
        columnplaceholder = Label(x, text="                                                               ", bg= "lightblue").grid(row = 0, column=8)

        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 3, column=1)
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 6, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 9, column=1) 
        row_placeholder = Label(x, text=" ", bg= "lightblue").grid(row = 12, column=1)
        court_number = Label(x, text="Court 1", bg= "lightblue", font=16).grid(row = 1, column=1)
        court_number = Label(x, text="Court 2", bg= "lightblue", font=16).grid(row = 4, column=1) 
        court_number = Label(x, text="Court 3", bg= "lightblue", font=16).grid(row = 7, column=1) 
        court_number = Label(x, text="Court 4", bg= "lightblue", font=16).grid(row = 10, column=1)
        court_number = Label(x, text="Court 5", bg= "lightblue", font=16).grid(row = 1, column=3)
        court_number = Label(x, text="Court 6", bg= "lightblue", font=16).grid(row = 4, column=3) 
        court_number = Label(x, text="Court 7", bg= "lightblue", font=16).grid(row = 7, column=3) 
        court_number = Label(x, text="Court 8", bg= "lightblue", font=16).grid(row = 10, column=3)
        court_number = Label(x, text="Court 9", bg= "lightblue", font=16).grid(row = 1, column=5)
        court_number = Label(x, text="Court 10", bg= "lightblue", font=16).grid(row = 4, column=5) 
        court_number = Label(x, text="Court 11", bg= "lightblue", font=16).grid(row = 7, column=5) 
        court_number = Label(x, text="Court 12", bg= "lightblue", font=16).grid(row = 10, column=5)
        court_number = Label(x, text="Court 13", bg= "lightblue", font=16).grid(row = 1, column=7)
        court_number = Label(x, text="Court 14", bg= "lightblue", font=16).grid(row = 4, column=7) 
        court_number = Label(x, text="Court 15", bg= "lightblue", font=16).grid(row = 7, column=7) 
        court_number = Label(x, text="Court 16", bg= "lightblue", font=16).grid(row = 10, column=7)
        court_number = Label(x, text="Court 17", bg= "lightblue", font=16).grid(row = 1, column=9)
        court_number = Label(x, text="Court 18", bg= "lightblue", font=16).grid(row = 4, column=9) 
        court_number = Label(x, text="Court 19", bg= "lightblue", font=16).grid(row = 7, column=9) 
        court_number = Label(x, text="Court 20", bg= "lightblue", font=16).grid(row = 10, column=9)
        
        court1 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court1.grid(row = 2, column=1)
        court2 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court2.grid(row = 5, column=1)
        court3 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court3.grid(row = 8, column=1)
        court4 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court4.grid(row = 11, column=1)
        court5 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court5.grid(row = 2, column=3)
        court6 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court6.grid(row = 5, column=3)
        court7 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court7.grid(row = 8, column=3)
        court8 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court8.grid(row = 11, column=3)
        court9 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court9.grid(row = 2, column=5)
        court10 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court10.grid(row = 5, column=5)
        court11 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court11.grid(row = 8, column=5)
        court12 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court12.grid(row = 11, column=5)
        court13 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court13.grid(row = 2, column=7)
        court14 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court14.grid(row = 5, column=7)
        court15 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court15.grid(row = 8, column=7)
        court16 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court16.grid(row = 11, column=7)
        court17 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court17.grid(row = 2, column=9)
        court18 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court18.grid(row = 5, column=9)
        court19 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court19.grid(row = 8, column=9)
        court20 = Text(x, width=15, height=10, font=16, bg = "#008B00")
        court20.grid(row = 11, column=9)

        dec_courtlist.append(court1)
        dec_courtlist.append(court2)
        dec_courtlist.append(court3)
        dec_courtlist.append(court4)
        dec_courtlist.append(court5)
        dec_courtlist.append(court6)
        dec_courtlist.append(court7)
        dec_courtlist.append(court8)
        dec_courtlist.append(court9)
        dec_courtlist.append(court10)
        dec_courtlist.append(court11)
        dec_courtlist.append(court12)
        dec_courtlist.append(court13)
        dec_courtlist.append(court14)
        dec_courtlist.append(court15)
        dec_courtlist.append(court16)
        dec_courtlist.append(court17)
        dec_courtlist.append(court18)
        dec_courtlist.append(court19)
        dec_courtlist.append(court20)

'''Booking Creator'''
def booking_insertion(name, number, month, day, timeslot, court_num, time_stamp, length_input): #Enters booking information into the employee display.
    
    time_slots = [['12AM', '1AM'], ['1AM', '2AM'], ['2AM', '3AM'], ['3AM', '4AM'], ['4AM', '5AM'], ['5AM', '6AM'], ['6AM', '7AM'], ['7AM', '8AM'], ['8AM', '9AM'], ['9AM', '10AM'], ['10AM', '11AM'], ['11AM', '12PM'], ['12PM', '1PM'], ['1PM', '2PM'], ['2PM', '3PM'], ['3PM', '4PM'], ['4PM', '5PM'], ['5PM', '6PM'], ['6PM', '7PM'], ['7PM', '8PM'], ['8PM', '9PM'], ['9PM', '10PM'], ['10PM', '11PM'], ['11PM', '12AM']]
    
    for x in time_slots:
        if x == timeslot:
            timeslot_index = time_slots.index(x)
    
    if month == "January":
        location = ((((day - 1) * 24) + timeslot_index) * 20) + (court_num - 1)
        if jan_courtlist[location].get(1.0, END) == "\n":
            jan_courtlist[location].insert(END, name + '\n')
            jan_courtlist[location].insert(END, number + '\n')
            jan_courtlist[location].insert(END, time_stamp[0] + " - " + time_stamp[1] + '\n')
            jan_courtlist[location].insert(END, "Booking ID: " + str(location) + '\n')
            jan_courtlist[location].config(bg="#00688B", fg="white")
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
    elif month ==  "February":
        location = ((((day - 1) * 24) + timeslot_index) * 20) + (court_num - 1)
        if feb_courtlist[location].get(1.0, END) == "\n":
            feb_courtlist[location].insert(END, name + '\n')
            feb_courtlist[location].insert(END, number + '\n')
            feb_courtlist[location].insert(END, time_stamp[0] + " - " + time_stamp[1] + '\n')
            feb_courtlist[location].insert(END, "Booking ID: " + str(location) + '\n')
            feb_courtlist[location].config(bg="#00688B", fg="white")
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
    elif month ==  "March":
        location = ((((day - 1) * 24) + timeslot_index) * 20) + (court_num - 1)
        if mar_courtlist[location].get(1.0, END) == "\n":
            mar_courtlist[location].insert(END, name + '\n')
            mar_courtlist[location].insert(END, number + '\n')
            mar_courtlist[location].insert(END, time_stamp[0] + " - " + time_stamp[1] + '\n')
            mar_courtlist[location].insert(END, "Booking ID: " + str(location) + '\n')
            mar_courtlist[location].config(bg="#00688B", fg="white")
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
    elif month == "April":
        location = ((((day - 1) * 24) + timeslot_index) * 20) + (court_num - 1)
        if apr_courtlist[location].get(1.0, END) == "\n":
            apr_courtlist[location].insert(END, name + '\n')
            apr_courtlist[location].insert(END, number + '\n')
            apr_courtlist[location].insert(END, time_stamp[0] + " - " + time_stamp[1] + '\n')
            apr_courtlist[location].insert(END, "Booking ID: " + str(location) + '\n')
            apr_courtlist[location].config(bg="#00688B", fg="white")
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
    elif month == "May":
        location = ((((day - 1) * 24) + timeslot_index) * 20) + (court_num - 1)
        if may_courtlist[location].get(1.0, END) == "\n":
            may_courtlist[location].insert(END, name + '\n')
            may_courtlist[location].insert(END, number + '\n')
            may_courtlist[location].insert(END, time_stamp[0] + " - " + time_stamp[1] + '\n')
            may_courtlist[location].insert(END, "Booking ID: " + str(location) + '\n')
            may_courtlist[location].config(bg="#00688B", fg="white")
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
    elif month ==  "June":
        location = ((((day - 1) * 24) + timeslot_index) * 20) + (court_num - 1)
        if jun_courtlist[location].get(1.0, END) == "\n":
            jun_courtlist[location].insert(END, name + '\n')
            jun_courtlist[location].insert(END, number + '\n')
            jun_courtlist[location].insert(END, time_stamp[0] + " - " + time_stamp[1] + '\n')
            jun_courtlist[location].insert(END, "Booking ID: " + str(location) + '\n')
            jun_courtlist[location].config(bg="#00688B", fg="white")
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
    elif month ==  "July":
        location = ((((day - 1) * 24) + timeslot_index) * 20) + (court_num - 1)
        if jul_courtlist[location].get(1.0, END) == "\n":
            jul_courtlist[location].insert(END, name + '\n')
            jul_courtlist[location].insert(END, number + '\n')
            jul_courtlist[location].insert(END, time_stamp[0] + " - " + time_stamp[1] + '\n')
            jul_courtlist[location].insert(END, "Booking ID: " + str(location) + '\n')
            jul_courtlist[location].config(bg="#00688B", fg="white")
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
    elif month ==  "August":
        location = ((((day - 1) * 24) + timeslot_index) * 20) + (court_num - 1)
        if aug_courtlist[location].get(1.0, END) == "\n":
            aug_courtlist[location].insert(END, name + '\n')
            aug_courtlist[location].insert(END, number + '\n')
            aug_courtlist[location].insert(END, time_stamp[0] + " - " + time_stamp[1] + '\n')
            aug_courtlist[location].insert(END, "Booking ID: " + str(location) + '\n')
            aug_courtlist[location].config(bg="#00688B", fg="white")
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
    elif month ==  "September":
        location = ((((day - 1) * 24) + timeslot_index) * 20) + (court_num - 1)
        if sep_courtlist[location].get(1.0, END) == "\n":
            sep_courtlist[location].insert(END, name + '\n')
            sep_courtlist[location].insert(END, number + '\n')
            sep_courtlist[location].insert(END, time_stamp[0] + " - " + time_stamp[1] + '\n')
            sep_courtlist[location].insert(END, "Booking ID: " + str(location) + '\n')
            sep_courtlist[location].config(bg="#00688B", fg="white")
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
    elif month ==  "October":
        location = ((((day - 1) * 24) + timeslot_index) * 20) + (court_num - 1)
        if oct_courtlist[location].get(1.0, END) == "\n":
            oct_courtlist[location].insert(END, name + '\n')
            oct_courtlist[location].insert(END, number + '\n')
            oct_courtlist[location].insert(END, time_stamp[0] + " - " + time_stamp[1] + '\n')
            oct_courtlist[location].insert(END, "Booking ID: " + str(location) + '\n')
            oct_courtlist[location].config(bg="#00688B", fg="white")
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
    elif month ==  "November":
        location = ((((day - 1) * 24) + timeslot_index) * 20) + (court_num - 1)
        if nov_courtlist[location].get(1.0, END) == "\n":
            nov_courtlist[location].insert(END, name + '\n')
            nov_courtlist[location].insert(END, number + '\n')
            nov_courtlist[location].insert(END, time_stamp[0] + " - " + time_stamp[1] + '\n')
            nov_courtlist[location].insert(END, "Booking ID: " + str(location) + '\n')
            nov_courtlist[location].config(bg="#00688B", fg="white")
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
    elif month ==  "December":
        location = ((((day - 1) * 24) + timeslot_index) * 20) + (court_num - 1)
        if dec_courtlist[location].get(1.0, END) == "\n":
            dec_courtlist[location].insert(END, name + '\n')
            dec_courtlist[location].insert(END, number + '\n')
            dec_courtlist[location].insert(END, time_stamp[0] + " - " + time_stamp[1] + '\n')
            dec_courtlist[location].insert(END, "Booking ID: " + str(location) + '\n')
            dec_courtlist[location].config(bg="#00688B", fg="white")
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
    if month == "January":
        if jan_courtlist[location].get(1.0, END) != "\n":
            jan_courtlist[location].delete(1.0, END)
            jan_courtlist[location].config(bg="#008B00")
        else:
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'There is no booking to cancel.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            jan_courtlist[location].config(bg="#008B00")
            error_window.mainloop()
    elif month ==  "February":
        if feb_courtlist[location].get(1.0, END) != "\n":
            feb_courtlist[location].delete(1.0, END)
            feb_courtlist[location].config(bg="#008B00")
        else:
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'There is no booking to cancel.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            feb_courtlist[location].config(bg="#008B00")
            error_window.mainloop()
    elif month == "March":
        if mar_courtlist[location].get(1.0, END) != "\n":
            mar_courtlist[location].delete(1.0, END)
            mar_courtlist[location].config(bg="#008B00")
        else:
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'There is no booking to cancel.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            mar_courtlist[location].config(bg="#008B00")
            error_window.mainloop()
    elif month == "April":
        if apr_courtlist[location].get(1.0, END) != "\n":
            apr_courtlist[location].delete(1.0, END)
            apr_courtlist[location].config(bg="#008B00")
        else:
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'There is no booking to cancel.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            apr_courtlist[location].config(bg="#008B00")
            error_window.mainloop()
    elif month == "May":
        if may_courtlist[location].get(1.0, END) != "\n":
            may_courtlist[location].delete(1.0, END)
            may_courtlist[location].config(bg="#008B00")
        else:
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'There is no booking to cancel.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            may_courtlist[location].config(bg="#008B00")
            error_window.mainloop()
    elif month ==  "June":
        if jun_courtlist[location].get(1.0, END) != "\n":
            jun_courtlist[location].delete(1.0, END)
            jun_courtlist[location].config(bg="#008B00")
        else:
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'There is no booking to cancel.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            jun_courtlist[location].config(bg="#008B00")
            error_window.mainloop()
    elif month ==  "July":
        if jul_courtlist[location].get(1.0, END) != "\n":
            jul_courtlist[location].delete(1.0, END)
            jul_courtlist[location].config(bg="#008B00")
        else:
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'There is no booking to cancel.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            jul_courtlist[location].config(bg="#008B00")
            error_window.mainloop()
    elif month ==  "August":
        if aug_courtlist[location].get(1.0, END) != "\n":
            aug_courtlist[location].delete(1.0, END)
            aug_courtlist[location].config(bg="#008B00")
        else:
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'There is no booking to cancel.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            aug_courtlist[location].config(bg="#008B00")
            error_window.mainloop()
    elif month ==  "September":
        if sep_courtlist[location].get(1.0, END) != "\n":
            sep_courtlist[location].delete(1.0, END)
            sep_courtlist[location].config(bg="#008B00")
        else:
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'There is no booking to cancel.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            sep_courtlist[location].config(bg="#008B00")
            error_window.mainloop()
    elif month ==  "October":
        if oct_courtlist[location].get(1.0, END) != "\n":
            oct_courtlist[location].delete(1.0, END)
            oct_courtlist[location].config(bg="#008B00")
        else:
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'There is no booking to cancel.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            oct_courtlist[location].config(bg="#008B00")
            error_window.mainloop()
    elif month ==  "November":
        if nov_courtlist[location].get(1.0, END) != "\n":
            nov_courtlist[location].delete(1.0, END)
            nov_courtlist[location].config(bg="#008B00")
        else:
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'There is no booking to cancel.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            nov_courtlist[location].config(bg="#008B00")
            error_window.mainloop()
    elif month ==  "December":
        if dec_courtlist[location].get(1.0, END) != "\n":
            dec_courtlist[location].delete(1.0, END)
            dec_courtlist[location].config(bg="#008B00")
        else:
            error_window = Toplevel()
            error_window.geometry("260x85")
            error_message = Label(error_window, text = 'ERROR:', fg="red", font=16).pack()
            help_message = Label(error_window, text = 'There is no booking to cancel.', fg="black", font=16).pack()
            exit_button = Button(error_window, text= "OK", command=error_window.destroy, fg="white", bg="#008B00", font=16).pack()
            dec_courtlist[location].config(bg="#008B00")
            error_window.mainloop() 

'''Start-up Booking Loader'''
def startup_insertion(input_name, input_num, location_code, input_month, timings): #Inserts bookings at startup to employee display. 
    code_num = int(location_code.strip('Location Code: '))

    if input_month == "January":
        jan_courtlist[code_num].insert(END, input_name + '\n')
        jan_courtlist[code_num].insert(END, input_num + '\n')
        jan_courtlist[code_num].insert(END, timings[0] + ' - ' + timings[1] + '\n')
        jan_courtlist[code_num].insert(END, "Booking ID: " + location_code.strip('Location Code: ') + '\n')
        jan_courtlist[code_num].config(bg="#00688B", fg="white")
    elif input_month == "February":
        feb_courtlist[code_num].insert(END, input_name + '\n')
        feb_courtlist[code_num].insert(END, input_num + '\n')
        feb_courtlist[code_num].insert(END, timings[0] + ' - ' + timings[1] + '\n')
        feb_courtlist[code_num].insert(END, "Booking ID: " + location_code.strip('Location Code: ') + '\n')
        feb_courtlist[code_num].config(bg="#00688B", fg="white")
    elif input_month == "March":
        mar_courtlist[code_num].insert(END, input_name + '\n')
        mar_courtlist[code_num].insert(END, input_num + '\n')
        mar_courtlist[code_num].insert(END, timings[0] + ' - ' + timings[1] + '\n')
        mar_courtlist[code_num].insert(END, "Booking ID: " + location_code.strip('Location Code: ') + '\n')
        mar_courtlist[code_num].config(bg="#00688B", fg="white")
    elif input_month == "April":
        apr_courtlist[code_num].insert(END, input_name + '\n')
        apr_courtlist[code_num].insert(END, input_num + '\n')
        apr_courtlist[code_num].insert(END, timings[0] + ' - ' + timings[1] + '\n')
        apr_courtlist[code_num].insert(END, "Booking ID: " + location_code.strip('Location Code: ') + '\n')
        apr_courtlist[code_num].config(bg="#00688B", fg="white")
    elif input_month == "May":
        may_courtlist[code_num].insert(END, input_name + '\n')
        may_courtlist[code_num].insert(END, input_num + '\n')
        may_courtlist[code_num].insert(END, timings[0] + ' - ' + timings[1] + '\n')
        may_courtlist[code_num].insert(END, "Booking ID: " + location_code.strip('Location Code: ') + '\n')
        may_courtlist[code_num].config(bg="#00688B", fg="white")
    elif input_month == "June":
        jun_courtlist[code_num].insert(END, input_name + '\n')
        jun_courtlist[code_num].insert(END, input_num + '\n')
        jun_courtlist[code_num].insert(END, timings[0] + ' - ' + timings[1] + '\n')
        jun_courtlist[code_num].insert(END, "Booking ID: " + location_code.strip('Location Code: ') + '\n')
        jun_courtlist[code_num].config(bg="#00688B", fg="white")
    elif input_month == "July":
        jul_courtlist[code_num].insert(END, input_name + '\n')
        jul_courtlist[code_num].insert(END, input_num + '\n')
        jul_courtlist[code_num].insert(END, timings[0] + ' - ' + timings[1] + '\n')
        jul_courtlist[code_num].insert(END, "Booking ID: " + location_code.strip('Location Code: ') + '\n')
        jul_courtlist[code_num].config(bg="#00688B", fg="white")
    elif input_month == "August":
        aug_courtlist[code_num].insert(END, input_name + '\n')
        aug_courtlist[code_num].insert(END, input_num + '\n')
        aug_courtlist[code_num].insert(END, timings[0] + ' - ' + timings[1] + '\n')
        aug_courtlist[code_num].insert(END, "Booking ID: " + location_code.strip('Location Code: ') + '\n')
        aug_courtlist[code_num].config(bg="#00688B", fg="white")
    elif input_month == "September":
        sep_courtlist[code_num].insert(END, input_name + '\n')
        sep_courtlist[code_num].insert(END, input_num + '\n')
        sep_courtlist[code_num].insert(END, timings[0] + ' - ' + timings[1] + '\n')
        sep_courtlist[code_num].insert(END, "Booking ID: " + location_code.strip('Location Code: ') + '\n')
        sep_courtlist[code_num].config(bg="#00688B", fg="white")
    elif input_month == "October":
        oct_courtlist[code_num].insert(END, input_name + '\n')
        oct_courtlist[code_num].insert(END, input_num + '\n')
        oct_courtlist[code_num].insert(END, timings[0] + ' - ' + timings[1] + '\n')
        oct_courtlist[code_num].insert(END, "Booking ID: " + location_code.strip('Location Code: ') + '\n')
        oct_courtlist[code_num].config(bg="#00688B", fg="white")
    elif input_month == "November":
        nov_courtlist[code_num].insert(END, input_name + '\n')
        nov_courtlist[code_num].insert(END, input_num + '\n')
        nov_courtlist[code_num].insert(END, timings[0] + ' - ' + timings[1] + '\n')
        nov_courtlist[code_num].insert(END, "Booking ID: " + location_code.strip('Location Code: ') + '\n')
        nov_courtlist[code_num].config(bg="#00688B", fg="white")
    elif input_month == "December":
        dec_courtlist[code_num].insert(END, input_name + '\n')
        dec_courtlist[code_num].insert(END, input_num + '\n')
        dec_courtlist[code_num].insert(END, timings[0] + ' - ' + timings[1] + '\n')
        dec_courtlist[code_num].insert(END, "Booking ID: " + location_code.strip('Location Code: ') + '\n')
        dec_courtlist[code_num].config(bg="#00688B", fg="white")

schedule_window.mainloop()
