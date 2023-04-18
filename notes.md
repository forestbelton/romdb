# ROM Database notes
These notes detail my efforts to extract game data from the global release of
Ragnarok Online M: Eternal Love 2.0 (ROM), a mobile game for Android/iOS
platforms.

## Zenhax forum posts
Some helpful information is available from forum threads on Zenhax:

- https://zenhax.com/viewtopic.php?t=8865
- https://zenhax.com/viewtopic.php?t=8887

Key takeaways:
- ROM was built in Unity
- Entity databases are stored under `resources/script2`
- [AssetStudio](https://github.com/Perfare/AssetStudio/) can extract
- Databases are encoded/encrypted in yet-unknown format
- Posts are about SEA version of the game

## Extracting the data
Following the steps described on Zenhax, I downloaded the APK for ROM from
[APKPure](https://apkpure.com/ragnarok-m-eternal-love-rom/com.gravity.romNAg),
one of many APK downloading websites. From the URL, it appears that the
package name for the game is `com.gravity.romNAg`.

Using Asset Studio to unpack the APK, I was unable to find any of the data
mentioned on Zenhax. In particular, the `script2` directory was nowhere to
be found. I downloaded the linked SEA version of the APK, and noticed that it
was 1.3GB, much larger than the 91.7MB global APK. It seems obvious at this
point that the data is downloaded and stored locally on the device during the
patching process, rather than being distributed with the APK.

Using the `Media Manager` application of my [BlueStacks](https://www.bluestacks.com/)
instance for the game, I navigated to the following path:

```
/sdcard/Android/data/com.gravity.romNAg/files/Android
```

There, I was able to find `resources/script2` and the files mentioned on the
thread. In particular, I found:

- `com.unity3d`
- `config.unity3d`
- `config_adventure_chengjiu_maoxian.unity3d`
- `config_equip_zhuangbei_kapian.unity3d`
- `config_event_shijian.unity3d`
- `config_gameplay_wanfa.unity3d`
- `config_hint_tishizhiyin.unity3d`
- `config_introduction_zhandoushouce.unity3d`
- `config_item_daoju.unity3d`
- `config_map_fuben.unity3d`
- `config_npc_mowu.unity3d`
- `config_pay_zhifu.unity3d`
- `config_pvp_jingjisai.unity3d`
- `config_resource_ziyuan.unity3d`
- `config_skill_jineng.unity3d`
- `framework.unity3d`
- `functionsystem.unity3d`
- `mconfig.unity3d`
- `net.unity3d`
- `refactory.unity3d`

Unpacking the `.unity3d` files with Asset Studio revealed the database files I
was looking for. Each file has the `TextAsset` type and a `.bytes` extension.

I started by inspecting `config_item_daoju.unity3d` to extract the item list.
It contained these files:

- `Table_AddWay`
- `Table_AdventureItem`
- `Table_Compose`
- `Table_Food`
- `Table_Growth`
- `Table_HeadwearRepair`
- `Table_Item`
- `Table_ItemAccess`
- `Table_ItemAdvManual`
- `Table_ItemDisplay`
- `Table_ItemRef`
- `Table_ItemType`
- `Table_ItemTypeAdventureLog`
- `Table_Preview`
- `Table_Recipe`
- `Table_Recommend`
- `Table_Reward`
- `Table_ServantImproveGroup`
- `Table_ServantUnlockFunction`
- `Table_TasterLevel`
- `Table_TwelvePvpTask`
- `Table_UseItem`
- `Table_UserBackground`
- `Table_UserChatFrame`
- `Table_UserPortraitFrame`
- `Table_Wallet`

Each file starts with a `'*'` byte and contains unknown binary data. Some files
have build filepaths from the development Jenkins server in them, and other
files appear to contain a JSON-like data structure at the bottom.

## Unity
The version used to build ROM was `2019.4.21f1XD`.
