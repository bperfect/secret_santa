import random
import smtplib
from email.mime.text import MIMEText

def get_emails(filename):
    """
    Reads in a file of names and email addresses
    Returns a list of pair<name,email>
    Format should be:
    <name 1>
    <email 1>
    <name 2>
    <email 2>
    ...
    """
    fin = open(filename, "r")
    lines = [ line.strip() for line in fin.readlines() ]
    assert len(lines)%2 == 0 # if it's in the right format...
    names  = [lines[i] for i in range(0, len(lines), 2)]
    emails = [lines[i+1] for i in range(0, len(lines), 2)]
    return zip(names, emails)

def send_gift_email( (gifter, gifter_email), (giftee, giftee_email) ):
    server = "localhost"
    from_address = "bperfect@hmc.edu"
    to_address = gifter_email
    subject = "Gift Exchange: Your giftee"
    text = """
    Hey guys,

    So here's the NEW Secret Santa email with the NEW person
    you should find a present for!

    You should find a present for %s!

    We'll exchange gifts after break, which gives you
    approximately forever to do shit. Gifts should be about $20
    (I think that's what we usually do. If you want to spend more,
    go for it ((your person probs won't complain))).

    Ho ho ho,
    Wuffles

    ((Sent by an automated script. I will cry if it breaks.))
    P.S. I don't even know who has who, for the record
    """ % giftee

    msg = MIMEText(text)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    s = smtplib.SMTP(server)
    s.sendmail(from_address, [to_address], msg.as_string())
    s.quit()
    

def send_emails(L):
    for i in range(len(L)):
        send_gift_email(L[i], L[(i+1)%len(L)])


def main():
    L = get_emails("emails.txt")
    a=False
    while a == False:
        a=True
        random.shuffle(L)
        for x in range(len(L)):
            if L[x][0] == "Brad" and L[(x+1)%len(L)][0] == "Matt Toal":
                a=False
            if L[x][0] == "Brad" and L[(x+1)%len(L)][0] == "Leslie":
                a=False
            if L[x][0] == "Leslie" and L[(x+1)%len(L)][0] == "Brad":
                a=False
            if L[x][0] == "Taylor" and L[(x+1)%len(L)][0] == "Matt Toal":
                a=False
            if L[x][0] == "Matt Toal" and L[(x+1)%len(L)][0] == "Taylor":
                a=False
            if L[x][0] == "Brad" and L[(x+1)%len(L)][0] == "Katie":
                a=False
            if L[x][0] == "Leslie" and L[(x+1)%len(L)][0] == "Tim":
                a=False
            if L[x][0] == "Katie" and L[(x+1)%len(L)][0] == "Leslie":
                a=False
            if L[x][0] == "Katie" and L[(x+1)%len(L)][0] == "Brad":
                a=False
        
    send_emails(L)
    fout=open("GE_log.log","w")
    print >>fout, L
    fout.close()

if __name__ == "__main__":
    main()
    
