#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import random
import tweepy
import os


def main():
    tokens = get_tokens()
    consumer_key = tokens["consumer_key"]
    consumer_secret = tokens["consumer_secret"]
    access_token = tokens["access_token"]
    access_token_secret = tokens["access_token_secret"]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    cont = 0
    has_failed = False
    lista_tweets = read_from_file()
    long = len(lista_tweets)
    while not has_failed:
        has_failed = False
        try:
            api.update_status(lista_tweets[cont % long])
            try:
                time.sleep(900)
                tweet = random_zxmast3r_tweet(api)
                api.update_status(tweet)
            except tweepy.error.TweepError as err:
                print(err)
            if not has_failed:
                time.sleep(900)
                cont += 1
        except tweepy.error.TweepError as err:
            print(err)
            cont += 1


def read_from_file():
    opened_file = open('gilipollas_bot.txt', 'rb')
    lista = []
    has_next = True
    while has_next:
        linea = opened_file.readline()
        if not linea:
            has_next = False
        else:
            lista.append(linea)
    return lista


def random_zxmast3r_tweet(api):
    tokens = get_tokens()
    lista = api.user_timeline(tokens["user_id"])
    tweet = ''
    contador = 0
    while len(tweet) < 75 and contador < len(lista):
        splitted = lista[contador].text.split()
        lines = len(splitted)
        random_pos = int(round(random.random() * lines, 0)) - 4
        cont = 0
        palabras = 0
        while palabras < 3 and cont < 20:
            word = splitted[(random_pos + cont) % lines]
            if 'http' not in word and 'RT' not in word and '@' not in word:
                tweet += ' ' + word
                palabras += 1
            cont += 1
        contador += 1
    return tweet


def get_tokens():
    if "CONSUMER_KEY" not in os.environ:
        exit("Error: Required Twitter Consumer Key...\nExit...")
    if "CONSUMER_SECRET" not in os.environ:
        exit("Error: Required Twitter Consumer Secret...\nExit...")
    if "ACCESS_TOKEN" not in os.environ:
        exit("Error: Required Twitter Access Token...\nExit...")
    if "ACCESS_TOKEN_SECRET" not in os.environ:
        exit("Error: Required Twitter Access Token Secret... \nExit...")
    if "USER_ID" not in os.environ:
        exit("Error: Required Twitter USER_ID... \nExit...")
    return {
        "consumer_key": os.environ["CONSUMER_KEY"],
        "consumer_secret": os.environ["CONSUMER_SECRET"],
        "access_token": os.environ["ACCESS_TOKEN"],
        "access_token_secret": os.environ["ACCESS_TOKEN_SECRET"],
        "user_id": os.environ["USER_ID"]
    }


if __name__ == "__main__":
    main()
