def main():
    print('################################################################################  WELCOME  TO  OUR  WORLD  ################################################################################')
    def passr(name,pas):
        f=open(r'C:\Users\user\OneDrive\Desktop\gona_reboot\login.txt','r+')
        rx=f.readlines()
        f.seek(0)
        f.flush()
        for i in rx:
            zx=i.split('-')
            if zx[0]!=name:
                f.write(i)
                continue
            elif zx[0]==name:
                del zx[1]
                zx+=['-'+pas+'\n']
                f.writelines(zx)
                f.flush()
                continue
        f.close
        return




    def passw():
        while True:
            user_pas=input("create a password :")
            if len(user_pas)<5:
                print('\t !!! password is too small !!!')
                continue
            if user_pas.isalpha() or user_pas.isdigit():
                print('\t !!! use both numeric and alphabets !!!\n')
                print('\t** you can also use special characters**')
                continue
                    
            user_pas_ch=input("Confirm your password :")
    
            if user_pas_ch==user_pas:
                print()
                break
            else:
                print()
                print("\t !!! Password doesn't match !!! ")
                print()
                continue
            break
        return user_pas    
            
    def admin():
        print('\t\t...................you are the creator of this world ...................\t\t')
        ad=['sritish','class20']
        admin_id=input('enter the admin id: ')
        admin_pas=input('enter the password: ')

    def login():
        while True:

        
            file=open(r'C:\Users\user\OneDrive\Desktop\gona_reboot\login.txt','r')
            print('''                        * 
                            * * 
                            * * * * 
                            * * * * *  
                        * * * * * * 
                        * * * * * * *   * * * *   * *     * * *  * * *
                            * *           *      *   *   *      *
                            * *           *      * *     * *    * *
                            * *           *      *   *   *      *
                            ** **          *      *    *  * * *  * * *
                        *************                    ''')
            print()
            print()
            print()
            start=input("                     USER or ADMIN : ").lower().rstrip()
            if start=='user':
                while True:
                    user_id=input('Enter your name :').rstrip().lower()
                    lx=file.readlines()
                    check=0
                    for i in lx:
                        
                        ax=i.split('-')
                        if ax[0]==user_id:
                            check=1
                            print('\t\t ** your name already exist **\n')
                            while True:
                                pasc=input('Do you want to reset your password: ').lower()
                                if pasc=='yes' or pasc=='y':
                                    px=passw()
                                    file.close()
                                    passr(user_id,px)
                                elif pasc=='no' or pasc=='n':
                                    rx=input('Enter the passowrd:')
                                    f=open(r'C:\Users\user\OneDrive\Desktop\gona_reboot\login.txt','r')
                                    rl=f.readlines()
                                    for i in rl:
                                        zl=i.split('-')
                                else:
                                    print("\t\t just write 'yes' or 'no'\n")
                                    continue
                                        

                                break
                    if check==0:
                        py=passw()
                        file=open(r'C:\Users\user\OneDrive\Desktop\gona_reboot\login.txt','a')
                        file.writelines([user_id+'-'+py+'\n'])
                        file.close()

                    break
            elif start=='admin':
                print('you are in admin page')
                admin()
            else:
                print('\t\t\t @-@-@ just write user or admin @-@-@\n\n')
                continue

            break

                
    def hom():
        print('you are in home page')
    
    login()
    hom()
main()