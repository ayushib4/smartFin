import 'package:flutter/material.dart';
import 'package:smart_fin_flutter/widgets/received_message.dart';
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
  bool visibility = true;

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

  void hideReactions() {
    setState(() {
      visibility = false;
    });
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
                "Ask Mr. Wonderful",
                style: TextStyle(
                  fontSize: 36,
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
            const Padding(
              padding: EdgeInsets.fromLTRB(16.0, 0.0, 16.0, 0.0),
              child: ReceivedMessage(
                  message:
                      "Hey there! I noticed you spent a lot of money at Apple this month (\$1K)."),
            ),
            Visibility(
              visible: visibility,
              child: Padding(
                padding: const EdgeInsets.fromLTRB(32.0, 8.0, 16.0, 0.0),
                child: Row(
                  children: [
                    OutlinedButton(
                      onPressed: () => hideReactions(),
                      child: const Icon(
                        Icons.thumb_up,
                        size: 20.0,
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.fromLTRB(8.0, 0.0, 0.0, 0.0),
                      child: OutlinedButton(
                        onPressed: () => hideReactions(),
                        child: const Icon(
                          Icons.thumb_down,
                          size: 20.0,
                        ),
                      ),
                    ),
                    Padding(
                      padding: const EdgeInsets.fromLTRB(8.0, 0.0, 0.0, 0.0),
                      child: OutlinedButton(
                        onPressed: () => hideReactions(),
                        child: const Icon(
                          Icons.tag_faces_rounded,
                          size: 20.0,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
            // const Padding(
            //   padding: EdgeInsets.fromLTRB(16.0, 8.0, 16.0, 16.0),
            //   child: TextField(
            //     decoration: InputDecoration(
            //       border: OutlineInputBorder(),
            //       labelText: 'Type your message here',
            //     ),
            //   ),
            // ),
          ],
        ),
      ),
    );
  }
}
