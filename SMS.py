from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

print("\033[91mBenvenuto e grazie per usare questo tool.\033[0m Visita https://github.com/VikingTerminal per provare altre utility.")

def invia_sms(account_sid, auth_token, destinatario_numero, tuo_numero_twilio, testo_messaggio):
    try:
        
        if not destinatario_numero.startswith('+') or not tuo_numero_twilio.startswith('+'):
            raise ValueError("\033[91mI numeri di telefono devono iniziare con un prefisso internazionale '+'.\033[0m")

        
        client = Client(account_sid, auth_token)

        
        message = client.messages.create(
            to=destinatario_numero,
            from_=tuo_numero_twilio,
            body=testo_messaggio
        )

        print(f'\033[92mMessaggio inviato con SID: {message.sid}\033[0m')

    except ValueError as ve:
        print(f"\033[91mErrore di input: {ve}\033[0m")
    except TwilioRestException as te:
        
        print(f"\033[91mErrore di Twilio: {te}\033[0m")
    except Exception as e:
        # Gestisci altre eccezioni generiche
        print(f"\033[91mSi è verificato un errore: {e}\033[0m")

if __name__ == "__main__":
    try:
        
        account_sid = input("\033[94mInserisci il tuo Account SID: \033[0m")
        auth_token = input("\033[94mInserisci il tuo Auth Token: \033[0m")
        destinatario_numero = input("\033[94mInserisci il numero del destinatario con prefisso internazionale: \033[0m")
        tuo_numero_twilio = input("\033[94mInserisci il tuo numero Twilio con prefisso internazionale: \033[0m")
        testo_messaggio = input("\033[94mInserisci il testo del messaggio: \033[0m")

        
        invia_sms(account_sid, auth_token, destinatario_numero, tuo_numero_twilio, testo_messaggio)

    except KeyboardInterrupt:
        print("\n\033[93mOperazione interrotta dall'utente.\033[0m")
    except Exception as e:
        print(f"\033[91mSi è verificato un errore generale: {e}\033[0m")
