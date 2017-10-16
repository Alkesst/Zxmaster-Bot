#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import time
import random
import tweepy


def main():
    json_config = open("tokens.json", 'r')
    tokens = json.load(json_config)
    json_config.close()
    consumer_key = tokens["consumer_key"]
    consumer_secret = tokens["consumer_secret"]
    access_token = tokens["access_token"]
    access_token_secret = tokens["access_token_secret"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    cont = 0
    while True:
        lista_tweets = read_from_file()
        api.update_status(lista_tweets[cont % len(lista_tweets)])
        time.sleep(900)
        tweet = random_ZXMAST3R_tweet(api)
        api.update_status(tweet)
        time.sleep(900)
        cont += 10


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


def random_ZXMAST3R_tweet(api):
    json_config = open("tokens.json", 'r')
    tokens = json.load(json_config)
    json_config.close()
    lista = api.user_timeline(tokens["user_id"])
    tweet = ''
    contador = 0
    while len(tweet) < 50 and contador < len(lista):
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


if __name__ == "__main__":
    main()
