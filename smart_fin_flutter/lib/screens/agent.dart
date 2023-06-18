import 'package:flutter/material.dart';
import 'package:video_player/video_player.dart';

class Agent extends StatefulWidget {
  const Agent({super.key, required this.mood});

  final String mood;

  @override
  State<Agent> createState() => _AgentState();
}

class _AgentState extends State<Agent> {
  List messages = [];
  late VideoPlayerController _controller;
  late Future<void> _initializeVideoPlayerFuture;

  @override
  void initState() {
    super.initState();

    String mood = widget.mood;

    _controller = VideoPlayerController.asset(
      'assets/videos/$mood.mov',
    )..setLooping(true);
    _controller.setVolume(0.0);

    _initializeVideoPlayerFuture = _controller.initialize().then(
          (value) => _controller.play(),
        );
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Padding(
              padding: EdgeInsets.all(16.0),
              child: Text(
                "Ask",
                style: TextStyle(
                  fontSize: 48,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            FutureBuilder(
              future: _initializeVideoPlayerFuture,
              builder: (context, snapshot) {
                if (snapshot.connectionState == ConnectionState.done) {
                  return AspectRatio(
                    aspectRatio: _controller.value.aspectRatio,
                    child: VideoPlayer(_controller),
                  );
                } else {
                  return const Center(
                    child: CircularProgressIndicator(),
                  );
                }
              },
            ),
            // AvatarGlow(
            //   endRadius: 60.0,
            //   child: Material(
            //     // Replace this child with your own
            //     elevation: 8.0,
            //     shape: const CircleBorder(),
            //     child: CircleAvatar(
            //       backgroundColor: Colors.grey[100],
            //       radius: 30.0,
            //       child: Image.network(
            //         'https://cdn-icons-png.flaticon.com/512/3135/3135715.png',
            //         height: 50,
            //       ),
            //     ),
            //   ),
            // ),
            // Padding(
            //   padding: EdgeInsets.fromLTRB(16.0, 8.0, 16.0, 8.0),
            //   child: ReceivedMessage(
            //       message:
            //           "Hey there! I noticed you spent a lot of money at Apple this month (\$1K). Can you tell me what you purchased and how necessary this purchase was?"),
            // ),
            const Padding(
              padding: EdgeInsets.fromLTRB(16.0, 8.0, 16.0, 16.0),
              child: TextField(
                decoration: InputDecoration(
                  border: OutlineInputBorder(),
                  labelText: 'Ask',
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
