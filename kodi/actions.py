from kodijson import Kodi as _Kodi
import time as _time


class KodiActions():
    def __init__(self, host):
        if host == 'living room':
            kodi_ip = '192.168.1.18'
        elif host == 'yonatan':
            kodi_ip = '192.168.1.115'
        else:
            return

        self._kodi = _Kodi('http://{}:8080/jsonrpc'.format(kodi_ip))

    def search_for_show_id(self, query):
        all_shows = self._kodi.VideoLibrary.GetTVShows()['result']['tvshows']
        for show in all_shows:
            if show['label'].lower() == query.lower():
                return show['tvshowid']
        return None

    def latest_unwatched_episode(self, tvshowid):
        all_episodes = self._kodi.VideoLibrary.GetEpisodes(tvshowid=tvshowid, properties=['playcount', 'resume', 'tvshowid'])[
            'result']
        if all_episodes.get('episodes') is None:
            return "TV Show Not Found"
        else:
            all_episodes = all_episodes.get('episodes')

        unwatched_episodes = filter(lambda x: x, [episode if episode['playcount'] == 0 else False for episode in all_episodes])
        if len(unwatched_episodes) == 0:
            return 'No Unwatched Episodes for selected show'
        return unwatched_episodes[0]['episodeid']

    def play_episode(self, episodeid):
        episode_location = self._kodi.VideoLibrary.GetEpisodeDetails(episodeid=episodeid, properties=['resume'])['result']['episodedetails']['resume']
        episode_percentage = 0 if episode_location['position'] == 0 else (episode_location['position'] - 15) * 100 / episode_location['total']
        self._kodi.Player.Open(item=dict(episodeid=episodeid))
        while self._kodi.Player.GetActivePlayers()['result']:
            pass
        player_id = filter(lambda y: y, [x if x['type'] == 'video' else None for x in self._kodi.Player.GetActivePlayers()['result']])[0]['playerid']
        _time.sleep(0.25)
        self._kodi.Player.Seek(playerid=player_id, value=episode_percentage)

    def play_latest_episode_of_show(self, tvshow):
        tvshowid = self.search_for_show_id(tvshow)
        episodeid = self.latest_unwatched_episode(tvshowid)
        self.play_episode(episodeid)

