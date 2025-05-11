const mongoose = require('mongoose');
const passportLocalMongoose = require('passport-local-mongoose');

const UserSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
    trim: true
  }
}, {
  timestamps: true
});

// Adds username, hash+salted password fields + auth methods
UserSchema.plugin(passportLocalMongoose, {
  usernameField: 'email', // Optional: use email instead of username
});

module.exports = mongoose.model('User', UserSchema);
