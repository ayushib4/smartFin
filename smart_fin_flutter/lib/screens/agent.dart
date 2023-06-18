import 'package:flutter/material.dart';
import 'package:smart_fin_flutter/widgets/received_message.dart';

class Agent extends StatefulWidget {
  const Agent({super.key});

  @override
  State<Agent> createState() => _AgentState();
}

class _AgentState extends State<Agent> {
  List messages = [];

  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Padding(
              padding: EdgeInsets.all(16.0),
              child: Text(
                "Ask",
                style: TextStyle(
                  fontSize: 48,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
            Padding(
              padding: EdgeInsets.fromLTRB(16.0, 8.0, 16.0, 8.0),
              child: ReceivedMessage(
                  message:
                      "Hey there! I noticed you spent a lot of money at Apple this month (\$1K). Can you tell me what you purchased and how necessary this purchase was?"),
            ),
            Padding(
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
